import random  

random_number = random.randint(1, 100)  
guess = 0

print("GUESSING GAME!")


while guess != random_number:
    guess = int(input("Try to guess the number: "))  
    if guess < random_number:
        print("Too low! Try again.")  
    elif guess > random_number:
        print("Too high! Try again.")  

print("Congratulations! Your guess is correct!!")
