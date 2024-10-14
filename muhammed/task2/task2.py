# q1

limit=int(input("enter the natural number"))
sum=0
for i in range(1,limit+1):
    sum+=i
print(f"the sum of the natural numbers up to {limit} is {sum}")


# q2

number=int(input("enter a non negative integer"))
factorial=1
for i in range(1,number+1):
    factorial*=i

print(f"{number} factorial is {factorial}")

# q3

string=input("enter the word")
vowels="aeiouAEIOU"
count=0
for i in string:
    if i in vowels:
      count+=1
    
print(f"the total number of vowels in the given word {string} is {count}")

# q4
n = int(input("Enter the limit for Fibonacci series: "))  
a, b = 0, 1  
print("Fibonacci Series:")
while a <= n:
    print(a, end=" ") 
    a, b = b, a + b 


# q5

number=int(input("\nenter the the number to check prime or not"))
is_prime= True
if number<=1:
    is_prime= not is_prime
else:
    for i in range(2,(number//2)+1):
        if number%2==0:
            is_prime= not is_prime
            break
if is_prime :
    print(f"the number {number} is prime")  
else:
    print(f"the number {number} in not prime")

# q6
num = int(input("Enter a number to reverse "))
reverse = 0 
while num > 0:
    last_digit = num % 10 
    reverse = (reverse * 10) + last_digit 
    num //= 10 

print(f"The reverse of the number is {reverse}")

# q7
import random

random_number=random.randint(1,100)
guess=0
while guess!=random_number:
    guess=int(input("enter the number"))
    if guess > random_number:
        print("high")
    elif guess < random_number:
        print("low")

print("hi you made a correct guess")

# q8
n = int(input("Enter a number to print its multiplication table: "))  
print(f"Multiplication Table for {n}")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")  



# q9
number=input("enter the number")
count=0
for i in number:
    count+=1

print(f"the number of digit is{count}")









# q10


string = input("Enter a string or number to check if it's a palindrome: ")
input_string = string.lower()
if input_string == input_string[::-1]:
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")
