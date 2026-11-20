# Sample calculator input: 8, 2, +. Rectangle input: length 5, width 3.

try:
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    if operation == "+":
        print("Result:", first_number + second_number)
    elif operation == "-":
        print("Result:", first_number - second_number)
    elif operation == "*":
        print("Result:", first_number * second_number)
    elif operation == "/":
        if second_number == 0:
            print("Cannot divide by zero.")
        else:
            print("Result:", first_number / second_number)
    else:
        print("Invalid operation.")

    length = float(input("Enter the rectangle length: "))
    width = float(input("Enter the rectangle width: "))
    print("Rectangle area:", length * width)
except ValueError:
    print("Please enter valid numbers.")
