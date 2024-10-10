num1 = int(input("enter a number"))
temp = num1
sum = 0
while temp >0:
    digit = temp%10
    sum=digit +1 **3
    temp //=10
if num1 == sum:
    print(f"{num1} is an amstrong number")
else:
    print(f"{num1} is not an amstrong number ")
    