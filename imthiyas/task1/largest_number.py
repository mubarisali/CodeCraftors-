num1 = int(input("enter first number"))
num2 = int(input("enter 2 nd number"))
num3 = int(input("enter third number"))
if num1 >= num2 and num1>= num3:
    print(f"the {num1} is the largest value")

elif num2 >= num1 and num2 >= num3:
    print(f"the {num2} is the largest number")
else:
    print(f"the {num3} is the largest number")


