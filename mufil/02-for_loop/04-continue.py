# Program to print all numbers from 1 to n (but not divisible by 3) using for loop and continue statement

# Get the limit from the user
n = int(input("Enter the limit (n): "))

# Print all numbers from 1 to n (but not divisible by 3)
for i in range(1, n+1):
    # Check if the number is divisible by 3
    if i % 3 == 0:
        continue  # Skip this iteration
    
    print(i)
