
num = int(input("Enter a number to reverse: ")) 
reverse = 0  


while num > 0:
    last_digit = num % 10 
    reverse = (reverse * 10) + last_digit 
    num //= 10 

print(f"The reverse of the number is: {reverse}")