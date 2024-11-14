for i in range (1,6):
    str = ""
    for j in range (1,6-i):
        str += "  "
    for j in range (1,2*i):
        str += "* "
    for j in range (1,6-i):
        str += "  "
    print(str)