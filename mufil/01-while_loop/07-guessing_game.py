# Write a program to guess a number using while loop

import random

number_to_guess = random.randint(0, 20)

print("Welcome! I'm thinking of a number between 0 and 20.")
print("Try to guess it, and I'll tell you if you are too high or too low.")

while True:
    user_guess = int(input("Your guess? "))

    if user_guess < number_to_guess:
        print("Too low!")
    elif user_guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations! You've found the number!")
        break
