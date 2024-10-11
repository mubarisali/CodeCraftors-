string = input("enter a string: ")
vowels = 'ioueaAEIOU'
num = 0
for i in string:
    if i in vowels:
        num += 1
print(num)
