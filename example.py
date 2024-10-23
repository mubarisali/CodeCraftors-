numbers = [1,2,3,4,5,6,7,8]
numbers.sort(key=lambda x: bin(x).count('1'))
print(numbers)
