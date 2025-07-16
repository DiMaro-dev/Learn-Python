# Number Guessing Game
# This is a simple number guessing game where the user has to guess a number between 1 and 100.

import random

number_to_guess = random.randint(1, 100)  # Random number between 1 and 100
attempts = 0  # Counter for attempts
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100. Try to guess it!")
while True:
    user_guess = input("Guess the number between 1 and 100: ") 
    attempts += 1  

    try:
        user_guess = int(user_guess)  # Convert input to integer
    except ValueError:
        print("Please enter a valid number.")
        continue

    if user_guess < 1 or user_guess > 100:
        print("Your guess is out of range. Please try again.")
    elif user_guess < number_to_guess:
        print("Too low! Try again.")
    elif user_guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        break