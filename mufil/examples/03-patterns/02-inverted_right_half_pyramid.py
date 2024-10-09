# write a program to print the following pattern

"""
* * * * *   
* * * *    
* * *     
* *      
*       
"""

for i in range ( 1, 6 ):
    str = ""            
    for j in range ( 1, 7 - i ):
        str += "* "
    print(str)

