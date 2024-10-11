# Program to print odd numbers using while loop
# Accept a number from user
num = int(input("Enter a number: "))

# Initialize the counter
i = 1

# Print odd numbers using while loop
while i <= num:
    # Check if the number is odd
    if i % 2 != 0:
        print(i)
    
    # Increment the counter
    i += 2
