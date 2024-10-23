# Program to check whether a number is armstrong or not

# Accept number from user
num = int(input("Enter a number: "))

# Initialize variables
temp = num
sum = 0

# Calculate the sum of the cubes of the digits
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# Check if the number is armstrong
if num == sum:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
