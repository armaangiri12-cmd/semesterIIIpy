# Sample input: 25 degrees Celsius. Sample output: 77.0 degrees Fahrenheit.

try:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
except ValueError:
    print("Please enter a valid temperature.")
