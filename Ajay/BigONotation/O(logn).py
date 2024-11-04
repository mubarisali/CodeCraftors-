# log of number is number ^ number = some number
# base of computer is 2
# so every number needs to be represented as power of 2


#iterative way
def log(n):
    count = 0
    while n>1:
        n = n//2
        count += 1
    return count

print(log(9))

#recursive way
def log_recursion(n):
    if n <= 1 :
        return 0
    
    return 1 + log(n//2)

print(log_recursion(8))