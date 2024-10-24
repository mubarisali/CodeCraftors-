# Program to check whether a number is an Armstrong number or not
#Armstrong number is a number in which all the sum of cubes of digits is equal to the number itself 
#Logic - 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 1 +125 + 27 = 153 which is equal to the original number

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
