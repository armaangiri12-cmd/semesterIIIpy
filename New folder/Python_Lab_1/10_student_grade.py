# Sample input: 86. Sample output: Grade B.

try:
    marks = float(input("Enter marks out of 100: "))

    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    else:
        print("Grade: F")
except ValueError:
    print("Please enter valid marks.")
