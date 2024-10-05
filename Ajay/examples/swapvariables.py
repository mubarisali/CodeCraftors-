x = 50
y = 100

print(f"Before swapping => x is {x} , y is {y}" )

z = y 
y = x 
x = z

print(f"After swapping  => x is {x} , y is {y}" )


#alternate method for swapping

a = 10 
b = 20

print(f"Before swapping => a is {a} , y is {b}" )

a , b  = b , a

print(f"Before swapping => a is {a} , y is {b}" )
