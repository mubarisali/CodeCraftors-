import sys

# Variables of different data types
num = 42
pi = 3.14159
letter = 'A'
is_active = True

# Output memory size of each variable
print(f"Memory allocated to integer: {sys.getsizeof(num)} bytes")
print(f"Memory allocated to float: {sys.getsizeof(pi)} bytes")
print(f"Memory allocated to char: {sys.getsizeof(letter)} bytes")
print(f"Memory allocated to boolean: {sys.getsizeof(is_active)} bytes")
