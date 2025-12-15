input_file = "backup.txt"
output_file = "names.txt"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

with open(output_file, "w", encoding="utf-8") as f:
    for line in lines:
        if len(line.strip()) < 15:
            f.write(line)

print("Done. Kept only lines with length > 15.")
