#unlike other languages variables are *not declared* prior to the use in Python.
#int , float , string , tuple , list , set , dictionary. 
x = 10
print(type(x))
x = "Ajay Joy"
print(type(x))
x = 3.14
print(type(x))

#all variables in Python are memory variables meaning variable 
#contains memory address where the data is stored.

number = 500 
print(id(number)) 
number += 2
print(id(number)) 

#swapping variables are easy in python
x = 1
y = 2

x , y = y , x

print(f"x = {x} , y = {y}")

print("**************************************************************************************")


import sys

# Integer data type
num = 42
print(f"Size of integer: {sys.getsizeof(num)} bytes")

# Float data type
pi = 3.14159
print(f"Size of float: {sys.getsizeof(pi)} bytes")

# Character data type (string of length 1)
letter = 'A'
print(f"Size of character: {sys.getsizeof(letter)} bytes")

# Boolean data type
is_active = True
print(f"Size of boolean: {sys.getsizeof(is_active)} bytes")
