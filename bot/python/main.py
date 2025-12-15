import discord
from discord.ext import commands, tasks
import asyncio
import aiohttp
import itertools
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
HYPIXEL_KEYS = os.getenv("HYPIXEL_KEYS").split(",")

MOJANG_UUID = "https://api.mojang.com/users/profiles/minecraft/{}"
HYPIXEL_STATUS = "https://api.hypixel.net/status"

KEY_LIMIT = 2
key_cycle = itertools.cycle(HYPIXEL_KEYS)
key_semaphores = {k: asyncio.Semaphore(KEY_LIMIT) for k in HYPIXEL_KEYS}

online_players = []

# ---------------- FETCH LOGIC ---------------- #

async def fetch_uuid(session, name):
    async with session.get(MOJANG_UUID.format(name)) as r:
        if r.status != 200:
            return None
        return (name, (await r.json())["id"])

async def check_status(session, name, uuid):
    key = next(key_cycle)
    async with key_semaphores[key]:
        params = {"key": key, "uuid": uuid}
        async with session.get(HYPIXEL_STATUS, params=params) as r:
            if r.status != 200:
                return None
            data = await r.json()
            if data.get("session", {}).get("online"):
                return name
    return None

async def fetch_online_players():
    with open("names.txt") as f:
        names = [n.strip() for n in f if n.strip()]

    async with aiohttp.ClientSession() as session:
        uuid_tasks = [fetch_uuid(session, n) for n in names]
        results = await asyncio.gather(*uuid_tasks)
        uuid_map = {n: u for n, u in results if u}

        status_tasks = [
            check_status(session, name, uuid)
            for name, uuid in uuid_map.items()
        ]

        online = await asyncio.gather(*status_tasks)

    return [p for p in online if p]

# ---------------- DISCORD ---------------- #

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} ready.")
    update_online.start()
    post_status.start()

@tasks.loop(seconds=60)
async def update_online():
    global online_players
    online_players = await fetch_online_players()

@tasks.loop(seconds=30)
async def post_status():
    channel = bot.get_channel(1450155613811249307)
    if not channel:
        return

    if online_players:
        await channel.send(
            f"🟢 Online ({len(online_players)}): {', '.join(online_players)}"
        )
    else:
        await channel.send("🔴 Nobody online")

bot.run(DISCORD_TOKEN)
