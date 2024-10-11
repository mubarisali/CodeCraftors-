n = int(input("Enter the number of rows: "))

for i in range(0,n):
    for j in range(5-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()