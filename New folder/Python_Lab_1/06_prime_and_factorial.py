# Sample input: 5. Sample output: prime; factorial = 120.

try:
    number = int(input("Enter a non-negative whole number: "))

    if number < 0:
        print("Please enter a non-negative number.")
    else:
        is_prime = number >= 2
        for divisor in range(2, number):
            if number % divisor == 0:
                is_prime = False
                break

        if is_prime:
            print(number, "is a prime number.")
        else:
            print(number, "is not a prime number.")

        factorial = 1
        for value in range(1, number + 1):
            factorial *= value
        print("Factorial:", factorial)
except ValueError:
    print("Please enter a whole number.")
