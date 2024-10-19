def find_non_repeating(arr):
    result = 0
    for num in arr:
        result ^= num  
    return result

arr = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5]
non_repeating = find_non_repeating(arr)
print(non_repeating)