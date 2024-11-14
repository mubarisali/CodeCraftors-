num = int(input("Enter a number : "))
sum = 0
str_num = str(num)
len_num = len(str_num)
number = num 

while number > 0:
    digit = number % 10
    sum  += (digit ** len_num) 
    number = number //10
    
if sum == num :
    print("Number is armstrong !")
else:
    print("Number is not armstrong!")
