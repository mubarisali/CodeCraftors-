# Program to find the minimum number in an array
def find_min(arr):
    """Function to find the minimum number in an array."""
    if len(arr) == 0:
        return None
    min_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_num:
            min_num = arr[i]
    return min_num


print(find_min([1, 2, 3, 4]))
print(find_min([]))
print(find_min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(find_min([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]))
print(find_min([100, -100, 1000, -1000, 10000, -10000]))
