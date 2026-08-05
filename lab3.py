import math
num1 = int(input("Enter first number: "))
print("num1 is:", num1)


print("menu")
print("1. Square")
print("2. cube")
print("3. Sqrt")
print("4. ceiling value")
print("5. Floor value")
print("6. Absolute value")
print("7. Type of the variable")
print("8. Memory address")

choice = int(input("Enter your choice: "))
if choice == 1:
    print(f"Square of {num1} is {num1 ** 2}")
elif choice == 2:
    print(f"Cube of {num1} is {num1 ** 3}")
elif choice == 3:
    print(f"Square root of {num1} is {math.sqrt(num1)}")
elif choice == 4:
    print(f"Ceiling value of {num1} is {math.ceil(num1)}")
elif choice == 5:
    print(f"Floor value of {num1} is {math.floor(num1)}")
elif choice == 6:
    print(f"Absolute value of {num1} is {abs(num1)}")
elif choice == 7:
    print(f"Type of {num1} is {type(num1)}")
elif choice == 8:
    print(f"Memory address of {num1} is {id(num1)}")



