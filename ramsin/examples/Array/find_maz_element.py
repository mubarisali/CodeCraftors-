def find_max(arr):
    if len(arr) == 0:
        return None
    max_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]
    return max_num


print(find_max([1, 2, 3, 4]))
print(find_max([]))
print(find_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_max([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
print(find_max([100, -100, 1000, -1000, 10000, -10000]))