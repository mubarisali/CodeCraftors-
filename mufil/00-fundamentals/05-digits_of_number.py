# Python program to find the digits of a number


# To take input from the user
num = int(input("Enter a number: "))

# To get the absolute value of the number
num = abs(num)

# To print the digits of the number
while num > 0:
    print(num % 10, end=",")
    num //= 10
print()

