# Simulating unsigned integer behavior in Python
num = int(input("Enter a positive integer: "))

if num < 0:
    print("Error: Only positive numbers are allowed (Unsigned Integer).")
else:
    print(f"The entered number is {num}")
