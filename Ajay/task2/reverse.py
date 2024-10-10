num = int(input("Enter a number: "))

if num<0:
    reversed_num = str(abs(num))[::-1]
    print(f"Reversed number is {-int(reversed_num)}")
elif num>0:
    reversed_num = str(num)[::-1]
    print(f"Reversed number is {int(reversed_num)}")
else:
    print("No reverse for zero!!")
    