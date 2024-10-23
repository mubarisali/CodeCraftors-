# 3.https://www.geeksforgeeks.org/problems/intersection-of-two-sorted-array-1587115620/1

def intersection(self, arr1, arr2):
    # Initialize two pointers
    i, j = 0, 0
    result = []
    
    # Iterate through both arrays
    while i < len(arr1) and j < len(arr2):
        # If both elements are equal, add to result
        if arr1[i] == arr2[j]:
            # Only add to result if it's not already there
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
        # If arr1's element is smaller, increment i
        elif arr1[i] < arr2[j]:
            i += 1
        # If arr2's element is smaller, increment j
        else:
            j += 1
    
    return result
print(intersection([1, 2, 3, 4, 5], [1, 2, 5, 7, 9]))