import sys
num = 42
pi = 3.14159
letter = 'A'
is_active = True
print(f"memmory allocation to integer: {sys.getsizeof(num)} bytes")
print(f"memmory allocation to float: {sys.getsizeof(pi)} bytes")
print(f"memmory allocation to charecter: {sys.getsizeof(letter)} bytes")
print(f"memmory allocation to boolean: {sys.getsizeof(is_active)} bytes")