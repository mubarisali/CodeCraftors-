### program1

name = "mubaris ali"
age = 21
is_student = True

print(f"Name: {name}, Age: {age}, Is_student: {is_student}")
is_student = not is_student

print(f"Name: {name}, Age: {age}, Is_student: {is_student} ")


###program2

data = 10
print("original value:",data)
print("original type:",type(data))
data = "hello"
print("updated value:",data)
print("updated type:",type(data))


##program4

import sys

int_var = 10
float_var = 3.14
char_var = 'a'
bool_var = True

print("Memory size of int:", sys.getsizeof(int_var))
print("Memory size of float:", sys.getsizeof(float_var))
print("Memory size of char:", sys.getsizeof(char_var))
print("Memory size of bool:", sys.getsizeof(bool_var))


##program5

number = int(input("enter number: "))
if number < 0:
    print("the number is negative.")
elif number > 0:
    print("the number is positive.")
elif number == 0:
    print("number is zero.")
else:
    print("input is not a number")    


    ##program6

name = input("enter your name: ")
age = int( input("enter your age: "))
print(f"hello {name}, you are {age} years old.")    


##program7

number = 10
pi = 3.14
print(f"Number: {number}, Type: {type(number)}")
print(f"pi: {pi}, Type: {type(pi)}")


##program8
a =int(input("enter first number: "))
b =int(input("enter second number: "))
c =int(input("enter third number: "))
if a >= b and a >= c:
    print(f"largest number is : {a}")
elif b >= a and b >=c:
    print(f"largest number is : {b}")  
else:
    print(f"largest number is : {c}")  

largest = max(a ,b ,c)
print(f"largest number using max() is:{largest}")        


##program9

num1 = input("enter first number: ")
num2 = input("enter second number: ")
sum = int(num1) + int(num2)
print("sum is: " + str(sum))