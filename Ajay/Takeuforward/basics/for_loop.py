#Iterating over a List
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit,end=" ")
print()    
#Iterating over a String
greeting = "Hello!"
for char in greeting:
    print(char,end=" ")
print()  
#Using range() in a for Loop
for i in range(1,6):
    print(i , end=" ")
print()
for i in range(2,11,2):
    print(i , end=" ")
print()
#Iterting over a dictionary 
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
for key in person:
    print(key , end=" ")
print()
for value in person.values():
    print(value , end=" ")
print()
for key,value in person.items():
    print(f"{key} : {value}" , end = " ")
print()
# break and continue in loops.
for i in range(1 , 6):
    if i == 5 :
        break
    print(i , end=" ")
print()
for i in range (1,6):
    if i == 3 :
        continue
    print(i , end=" ")
print()
    