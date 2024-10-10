# write a program to print the following pattern

"""
* * * * *   
* * * *    
* * *     
* *      
*       
"""
# solution 1
for i in range ( 1, 6 ):
    str = ""            
    for j in range ( 1, 7 - i ):
        str += "* "
    print(str)

# solution 2

for i in range (6):
    str = ""            
    for j in range (5-i):
        str += "* "
    print(str)