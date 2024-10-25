#immutable objects behaves as pass by value
def add(x):
    x = x+10
    print(f"Value of x inside add function is {x}")
    
x = 5 
print(f"Value of x outside add function is {x}")

add(x)


#mutable objects behaves as pass by reference

def modify_list(list):
    list.append(10)
    print(f"List inside the function after appending is {list}")
    
list = [1,2,3,4,5,6]
modify_list(list)
print(f"List outside the function will reflect the change {list}")
    