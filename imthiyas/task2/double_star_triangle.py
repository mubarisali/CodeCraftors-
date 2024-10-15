for i in range(1 , 11):
    str=""
    if (i < 6):
        for j in range(1,7-i):
            str +="*"
    else:
        for j in range(1,i-4):
            str +="*"
    print(str)