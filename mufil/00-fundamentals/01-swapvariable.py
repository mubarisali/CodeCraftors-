a=10 
b=5
print(f"Before Swap : a={a} , b={b}")

c=a
a=b
b=c

print(f"After Swap : a={a} , b={b}")


x = 10
y = 20

print(f"Before Swap : x={x} , y={y}")

x, y = y, x

print(f"After Swap : x={x} , y={y}")


p = 2
q = 3

print(f"Before Swap : p={p} , q={q}")

p = p + q
q = p - q
p = p - q

print(f"After Swap : p={p} , q={q}")