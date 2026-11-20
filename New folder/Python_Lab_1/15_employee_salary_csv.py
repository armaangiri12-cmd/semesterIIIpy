# Reads employees.csv and calculates HRA (20%), DA (10%), and gross salary.

import csv
from pathlib import Path

csv_path = Path(__file__).with_name("employees.csv")

with csv_path.open("r", newline="", encoding="utf-8") as csv_file:
    employees = csv.DictReader(csv_file)
    for employee in employees:
        basic_salary = float(employee["basic_salary"])
        hra = basic_salary * 0.20
        da = basic_salary * 0.10
        gross_salary = basic_salary + hra + da
        print(employee["name"], "- Gross salary:", format(gross_salary, ".2f"))
