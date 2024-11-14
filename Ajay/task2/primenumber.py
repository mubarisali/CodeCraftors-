num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
else:
    is_prime = True  
    for i in range(2, int(num ** 0.5) + 1): #square root of any number is enough
        if num % i == 0:
            print("Number is not a prime number")
            is_prime = False  
            break  

    if is_prime:
        print("Number is a prime number")


   