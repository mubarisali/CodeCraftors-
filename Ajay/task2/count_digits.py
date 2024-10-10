num = int(input("Enter a number ")) 
number = abs(num)
digit_count = 0 


while number > 0:
    number //= 10 
    digit_count += 1  

print(f"The number of digits in {num} is - {digit_count}")
