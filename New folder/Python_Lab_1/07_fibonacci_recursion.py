# Sample input: 7. Sample output: 0 1 1 2 3 5 8

def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


try:
    count = int(input("How many Fibonacci terms should be displayed (0-30)? "))
    if count < 0 or count > 30:
        print("Please enter a number from 0 to 30.")
    else:
        series = [fibonacci(index) for index in range(count)]
        print("Fibonacci series:", *series)
except ValueError:
    print("Please enter a whole number.")
