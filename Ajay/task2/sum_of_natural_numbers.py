num = int(input("Enter the limit : "))

if num > 0:
    sum = int (num  * (num + 1) / 2)
    print(f"Sum of natural numbers upto {num} is {sum}")

else:
    print("Sorry ..negative number/zero")