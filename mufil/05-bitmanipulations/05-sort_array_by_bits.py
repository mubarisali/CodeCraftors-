#https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/description/

#solution -1 

def sortByBits1(arr):
    def countBits(val):
        count = 0
        while val > 0:
            if val & 1 == 1:
                count += 1
            val = val >> 1
        return count

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if (countBits(arr[j]), arr[j]) > (countBits(arr[j+1]), arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

# solution 2

def sortByBits2(arr):
    def countBits(val):
        count = 0
        while val > 0:
            if val & 1 == 1:
                count += 1
            val = val >> 1
        return count

    arr.sort(key=lambda x: (countBits(x), x))
    return arr

# solution 3

def sortByBits3(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr

print(sortByBits1([0,1,2,3,4,5,6,7,8]))