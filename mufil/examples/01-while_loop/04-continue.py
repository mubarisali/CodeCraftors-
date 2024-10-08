# Program to print all numbers from 1 to n (but not divisible by 5) using while loop and continue statement

# Get the limit from the user
n = int(input("Enter the limit (n): "))

# Initialize the counter
i = 1

# Print all numbers from 1 to n (but not divisible by 5)
while i <= n:
    # Check if the number is divisible by 5
    if i % 5 == 0:
        i += 1
        continue  # Skip this iteration
    
    print(i)
    i += 1
