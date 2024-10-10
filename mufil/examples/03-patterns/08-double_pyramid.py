# write a program to print the following pattern - double pyramid

"""
*         *  
* *       * *  
* * *     * * *  
* * * *   * * * *    
* * * * * * * * * *   
"""

for i in range (1,6):
    str = ""
    for j in range (1,i+1):
        str+="* "
    for j in range (1,6-i):
        str+="  "
    for j in range (1,i+1):
        str+="* "
    print(str)
