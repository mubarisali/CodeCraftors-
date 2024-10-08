n = int(input("enter positive integer: "))
factorial = 1
counter = 1
while counter <= n:
    factorial *= counter
    counter += 1
print(f"factorial of {n} is: {factorial}")    