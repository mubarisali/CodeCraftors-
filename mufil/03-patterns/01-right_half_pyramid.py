# write a prgram to print the following pattern - right half pyramid

"""
*           
* *         
* * *       
* * * *    
* * * * *   
"""

for i in range ( 1, 6 ):
    str = ""            
    for j in range ( 1, i + 1 ):
        str += "* "
    print(str)

# solution 2

for i in range (6):
    str = ""            
    for j in range (i):
        str += "* "
    print(str)
print()

# solution 3

i = 1
while i <= 5:
    str = ""
    j = 1
    while j <= i:
        str += "* "
        j += 1
    print(str)
    i += 1