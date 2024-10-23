# Program to print numbers from 1 to n, and break the loop when the number matches the breaking number

# Get the limit and breaking number from the user
n = int(input("Enter the limit (n): "))
breaking_number = int(input("Enter the breaking number: "))

# Print numbers from 1 to n
for i in range(1, n+1):
    # Check if the number matches the breaking number
    if i == breaking_number:
        print(f"Breaking at {i}")
        break
    print(i)
