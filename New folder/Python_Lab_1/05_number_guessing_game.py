# Guess a number from 1 to 100. You have six attempts.

import random

secret_number = random.randint(1, 100)
maximum_attempts = 6

print("I am thinking of a number from 1 to 100.")

for attempt in range(1, maximum_attempts + 1):
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a whole number.")
        continue

    if guess < 1 or guess > 100:
        print("Enter a number from 1 to 100.")
    elif guess == secret_number:
        print("Correct! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low.")
    else:
        print("Too high.")

    if attempt == maximum_attempts:
        print("Out of attempts. The number was", secret_number)
