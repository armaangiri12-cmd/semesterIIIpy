# Reads and displays the sample log stored beside this program.

from pathlib import Path

log_path = Path(__file__).with_name("sample.log")

with log_path.open("r", encoding="utf-8") as log_file:
    print(log_file.read(), end="")
