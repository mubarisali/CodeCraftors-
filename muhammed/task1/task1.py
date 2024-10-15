# question 1

name="muhammed"
age=23
is_student=True

print(f"\nname is {name} age is {age} ,is Student: {is_student}")

is_student=not is_student


print(f"\nname is {name} age is {age} ,is Student: {is_student}")

# q2

data=200
print(f"\nintial value is {data},type is {type(data)}")

data="muhammed"

print(f"\nfinal value is {data},type is {type(data)}")

# q3
try:
    result=10/0
except:
    print("\nzero divison error")

# q4

import sys

num = 4
pi = 3.14159
letter = 'b'
is_active = True

print(f"\nMemory allocated to num: {sys.getsizeof(num)} bytes")
print(f"\nMemory allocated to pi: {sys.getsizeof(pi)} bytes")
print(f"\nMemory allocated to letter: {sys.getsizeof(letter)} bytes")
print(f"\nMemory allocated to is_active: {sys.getsizeof(is_active)} bytes")

# q5
num = int(input("Enter a positive number : "))
if num > 0:
    print(f"The entered number is {num}")
   
else:
    print("positive numbers are only  allowed")

# q6
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}, you are {age} years old.")


#q8
num1= int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 >= num2:
    if num1>=num3:
        print(f"\nthe largest number is {num1}")
elif num2>=num3:
    print(f"\nthe largest number is {num2}")
else:
    print(f"the largest number is {num3}")

# q9

num1 =int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sum_of_numbers = num1 + num2
print("The sum is: " + str(sum_of_numbers))



large_number = 123456789012345678901234567890

print(f"Large number: {large_number}")
print(f"Type of large_number: {type(large_number)}")
