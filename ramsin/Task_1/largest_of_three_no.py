num1 = int(input("Enter the 1st number : "))
num2 = int(input("Enter the 2nd number : "))
num3 = int(input("Enter the 3rd number : "))

if num1 > num2 and num1 > num3 :
    print(f"{num1} is the largest")
    
elif num2 > num1 and num2 > num3 :
    print(f"{num2} is the largest")
    
else:
    print(f"{num3} is the largest")
  
#print(f"Largest of the three is {max(num1,num2,num3)}")