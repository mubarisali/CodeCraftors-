# increasing triangle
rows=int(input("enter the number of rows"))
for i in range(1,rows+1):
    str=""
    for j in range(1,i+1):
        str+="* "
    print(str)

#decreasing triangle

rows=int(input("enter the number of rows for decreasing triangle"))
for i in range (rows):
    str=""
    for j in range(rows-i):
        str+="* "
    print(str)


# right sided downward triangle
rows=int(input("enter the no of rows of right sided downward triangle"))
for i in range(rows):
    star=""
    space=""
    for j in range(i):
         space+="  "
    print(space,end="")
    for k in range(rows-i):
        star+="* "
    print(star)

# right sided triangle 
rows=int(input("enter the no of rows for the right sided traingle"))
for i in range(rows):
    star=""
    space=""
    for j in range(rows-i-1):
        space+="  "
    print(space,end="")
    for k in range(i+1):
        star+="* "
    print(star)

# pyramid 

rows=int(input("enter the no of rows for the pyramid"))
for i in range(rows):
    star=""
    space=""
    for j in range(rows-i-1):
        space+=" "
    print(space,end=" ")
    for k in range(i+1):
        star+="* "
    print(star)

