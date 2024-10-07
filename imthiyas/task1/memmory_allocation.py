import sys
num = 10
pi = 3.14
letter = "A"
is_good = True

print(f"memmory allocation to integer: {sys.getsizeof(num)}bytes")
print(f"memmory allocation to float: {sys.getsizeof(pi)}bytes")
print(f"memmory allocation to charecter: {sys.getsizeof(letter)}bytes")
print(f"memmory allocation to boolean: {sys.getsizeof(is_good)}bytes")