# Python Lab 1 - 20 Experiments

Beginner-friendly Python programs covering fundamental programming concepts,
collections, file handling, classes, random numbers, and data visualization.

## Experiments

| No. | Experiment | Filename | Concepts |
| --- | --- | --- | --- |
| 1 | Basic Python program | `01_basic_python_program.py` | `print`, program execution |
| 2 | Arithmetic operations | `02_arithmetic_operations.py` | Variables, arithmetic operators |
| 3 | Calculator and rectangle area | `03_calculator_and_rectangle_area.py` | Input, conditionals, arithmetic |
| 4 | Temperature converter | `04_temperature_converter.py` | Numeric input, Celsius-to-Fahrenheit formula |
| 5 | Number guessing game | `05_number_guessing_game.py` | `random`, loops, conditionals |
| 6 | Prime and factorial | `06_prime_and_factorial.py` | Loops, divisibility, factorial |
| 7 | Fibonacci recursion | `07_fibonacci_recursion.py` | Recursive functions, lists |
| 8 | Random OTP | `08_random_otp.py` | Random six-digit number |
| 9 | Contact book | `09_contact_book.py` | Dictionaries, search, add, delete |
| 10 | Student grade | `10_student_grade.py` | Conditional grade calculation |
| 11 | List frequency | `11_list_frequency.py` | Lists, dictionaries, counting |
| 12 | Attendance management | `12_attendance_management.py` | Dictionaries, menus, attendance records |
| 13 | Read a log file | `13_read_log_file.py` | Text-file reading |
| 14 | Student details in a file | `14_student_details_files.py` | Input, text-file writing and reading |
| 15 | Employee salary from CSV | `15_employee_salary_csv.py` | CSV reading, salary calculation |
| 16 | System logs in JSON | `16_system_logs_json.py` | JSON reading, log analysis |
| 17 | Bank account class | `17_bank_account_class.py` | Classes, objects, deposit, withdrawal |
| 18 | Book management class | `18_book_management_class.py` | Classes, objects, book status |
| 19 | Dice rolling | `19_dice_rolling.py` | Random numbers |
| 20 | Retail sales bar chart | `20_retail_sales_bar_chart.py` | Sample data, Matplotlib bar chart |

## Sample data files

- `sample.log` is read by experiment 13.
- `employees.csv` is read by experiment 15. Gross salary is calculated as
  basic salary plus 20% HRA and 10% DA.
- `system_logs.json` is read and analyzed by experiment 16.
- Experiment 14 creates `student_details.txt` with the details entered when it
  is run.
- Experiment 20 saves `retail_sales_chart.png` beside the program.

## Running the programs

Run a program from this directory with Python 3:

```text
python 01_basic_python_program.py
```

Replace the filename with the experiment you want to run. Programs that request
input will prompt in the terminal. Experiment 20 requires Matplotlib; install
it with `python -m pip install matplotlib` if it is not already available.
The chart opens using Matplotlib's display window and is also saved as a PNG.
