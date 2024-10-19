n=5

for i in range(1,n+1):
    for j in range(1,6-i):
        print("   ",end=" ")
    for j in range(1,2*i):
        print(" * ",end=" ")
    for j in range(1,6-i):
        print("   ",end=" ")
    print()
        
        
print("----------------------------------------------------------------------")

for i in range(1, n + 1):
    for j in range(1, 6 - i):
        print("   ", end=" ") 
    for j in range(1, 2 * i):
        if j % 2 == 1: 
            print(" * ", end=" ")
        else:  
            print("   ", end=" ")
    for j in range(1, 6 - i):
        print("   ", end=" ") 
    print()