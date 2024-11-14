n = int(input("enter a number"))
reverse = 0

while n>0:
   
   last_digit = n % 10
   reverse = (reverse*10)+last_digit
   n //=10

   
print(f"{reverse}")