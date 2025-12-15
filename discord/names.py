print("SCRIPT STARTED")
import requests
import time

HYPIXEL_KEY = "YOUR_HYPIXEL_API_KEY"

INPUT_FILE = "existing_3_letter_names.txt"
OUTPUT_FILE = "hypixel_3_letter_names.txt"

MOJANG_URL = "https://api.mojang.com/users/profiles/minecraft/{}"
HYPIXEL_PLAYER_URL = "https://api.hypixel.net/player"

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    names = [line.strip() for line in f if line.strip()]

for name in names:
    # 1️⃣ Username -> UUID
    r = requests.get(MOJANG_URL.format(name))
    if r.status_code != 200:
        continue

    uuid = r.json()["id"]

    # 2️⃣ Check if player has ever joined Hypixel
    params = {
        "key": HYPIXEL_KEY,
        "uuid": uuid
    }

    r = requests.get(HYPIXEL_PLAYER_URL, params=params)
    if r.status_code != 200:
        print("Hypixel API error, stopping.")
        break

    data = r.json()

    if data.get("player") is not None:
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(name + "\n")
        print(f"FOUND ON HYPIXEL → {name}")

    time.sleep(0.5)  # ~110 req/min (safe)

print("Done. Hypixel players saved.")

