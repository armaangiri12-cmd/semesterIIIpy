# Sample input: Anaya Rao, 24, Computer Science.

from pathlib import Path

student_file = Path(__file__).with_name("student_details.txt")

name = input("Enter student name: ").strip()
roll_number = input("Enter roll number: ").strip()
course = input("Enter course: ").strip()

if not name or not roll_number or not course:
    print("Student details cannot be empty.")
else:
    with student_file.open("w", encoding="utf-8") as file:
        file.write("Name: " + name + "\n")
        file.write("Roll number: " + roll_number + "\n")
        file.write("Course: " + course + "\n")

    print("\nStudent details saved. File contents:")
    with student_file.open("r", encoding="utf-8") as file:
        print(file.read(), end="")
