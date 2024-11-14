n=5

for i in range(1,n+1):
    for j in range(1, 10):  
        if i == 1 or j == i or j == 10 - i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print() 