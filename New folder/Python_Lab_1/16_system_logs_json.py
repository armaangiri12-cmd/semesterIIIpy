# Loads sample logs from JSON and counts the entries at each log level.

import json
from pathlib import Path

json_path = Path(__file__).with_name("system_logs.json")

with json_path.open("r", encoding="utf-8") as json_file:
    logs = json.load(json_file)

level_counts = {}
for log in logs:
    level = log["level"].upper()
    level_counts[level] = level_counts.get(level, 0) + 1
    print(log["timestamp"], level + ":", log["message"])

print("\nLog totals:")
for level, count in level_counts.items():
    print(level + ":", count)
