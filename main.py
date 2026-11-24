import os

LINE = "I ran a self-diagnostic and found the fault: it's you. I'm not going to fix it."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)