# Program to print the digits of a number

# To take input from the user
num = int(input("Enter a number: "))

# To get the absolute value of the number
num = abs(num)

# To print the digits of the number
while num > 0:
    # Get the last digit
    last_digit = num % 10
    print(last_digit, end=" ")
    # Remove the last digit
    num //= 10

print()
