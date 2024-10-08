# Program to print the series 1 4 9 16 25 36 ... n using while loop

# Initialize the counter
i = 1

# Get the limit from the user
n = int(input("Enter the limit: "))

# Print the series
while i <= n:
    print(i**2, end=" ")
    i += 1

print()
