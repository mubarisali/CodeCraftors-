# Program to print the series 1 8 27 64 125  ... n using for loop

# Ask user for the limit
n = int(input("Enter the limit (n): "))

# Print the series
for i in range(1, n+1):
    # Calculate cube of number 
    cube = i**3
    # Print the current term
    print(cube, end=" ")

print()
