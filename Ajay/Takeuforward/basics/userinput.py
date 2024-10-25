#user input in python

x = int(input("Input first number: "))
print(type(x)) #input() takes everything as string so type is <class 'str'>.
y = int(input("Input second number :"))

print(x+y)

#Takes only the first character, ensuring only one character is taken from the input.
a = input("Enter a character: ")[0]
print(a)