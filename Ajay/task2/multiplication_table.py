num =int(input("Enter a positive number : "))

if num > 0 :
    print(f"Multiplication table of {num}\n")
    for i in range (1,11):
     print(f"{i} * {num} = {num*i}")
     
else:
    print("Enter a positive number!")