n = int(input("Enter the limit : "))

for i in range (0, n):
     for j in range(0 , i):
        print("   " , end = " ")
     for j in range(0 , 5-i):
        print(" * ",end=" ")
     print()