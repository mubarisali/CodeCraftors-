n=5

for i in range(1,n+1):
    for j in range(1,i):
        print("   ",end=" ")
    for j in range(1,12-2*i):
        print(" * ",end=" ")
    for j in range(1,i):
        print("   ",end=" ")
    
    print()