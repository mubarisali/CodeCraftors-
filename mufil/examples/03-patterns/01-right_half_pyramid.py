# write a prgram to print the following pattern

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

