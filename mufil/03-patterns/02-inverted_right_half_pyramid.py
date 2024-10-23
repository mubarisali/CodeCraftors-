# write a program to print the following pattern - inverted right half pyramid

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
print()

# solution 2

for i in range (6):
    str = ""            
    for j in range (5-i):
        str += "* "
    print(str)

# solution 3
i = 1
while i <= 5:
    str = ""
    j = 1
    while j <= 6-i:
        str += "* "
        j += 1
    print(str)
    i += 1