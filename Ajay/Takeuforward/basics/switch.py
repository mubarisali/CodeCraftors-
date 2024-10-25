def switch(value):
    switch = {
       1 : "One",
       2 : "Two",
       3 : "Three" 
    }
    
    return switch.get(value , "Invalid value")
    
    
num = int(input("Enter a number : "))

print (switch(num))