# write a program to print the following pattern - hollow fully inverted pyramid

"""
* * * * * * * * *   
  *           *   
    *       *   
      *   *   
        *   
"""

for i in range (1,6):
    str = ""
    for j in range (1,10):
        if i == 1 or j == i or j == 10-i : str += "* "
        else: str += "  "
    print(str)