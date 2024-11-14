# write a program to print the following pattern - fully inverted pyramid

"""
* * * * * * * * *   
  * * * * * * *   
    * * * * *   
      * * *   
        *   
"""

for i in range (1,6):
    str = ""
    for j in range (1,i):
        str += "  "
    for j in range (1,12-2*i):
        str += "* "
    print(str)
