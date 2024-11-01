#Example of nlogn 

n= 4 

y = n

while n > 1 :
    n = n //2
    for i in range(y):
        print(f"{i}",end=" ")
        
#Outer loop has a complexity of O(logn)
#Inner loop has a complexity of O(n)
#So total complexity is O(n*logn)