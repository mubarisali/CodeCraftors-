n = 5  # Number of rows

for i in range(1,n+1):
    for j in range (1 , i+1):
        print(" * ",end = " ")
    print()

print("------------------------------------------------------")   
     
for i in range(1,n+1):
    for j in range (1 , 7-i):
        print(" * ",end = " ")
    print()
        
print("------------------------------------------------------")   

for i in range(1,n+1):
    for j in range(1,6-i):
        print("   ",end=" ")  
    for j in range(1,i+1):
        print(" * " , end=" ")
    print()
    
print("------------------------------------------------------")

for i in range(1, n+1):
    for j in range(1,i):
        print("   ",end=" ")
    for j in range(1,7-i):
        print(" * ",end=" ")
    print()
    
print("------------------------------------------------------")