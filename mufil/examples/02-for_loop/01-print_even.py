# Program to print even numbers from 2 to n

# Ask user for the limit
n = int(input("Enter the limit (n): "))

# Print even numbers
for i in range(2, n+1):
    # Check if the number is even
    if i % 2 == 0:
        print(i)
