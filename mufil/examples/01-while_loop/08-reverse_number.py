# Program to return the reverse of a number

# Accept a number from user
num = int(input("Enter a number: "))

# Initialize variables
reverse = 0
temp = num

# Calculate the reverse of the number
while temp > 0:
    last_digit = temp % 10
    reverse = (reverse * 10) + last_digit
    temp //= 10

# Print the reverse of the number
print(f"Reverse of {num} is {reverse}")
