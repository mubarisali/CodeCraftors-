# 1.https://www.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1

def get_min_max(self, arr):
    if not arr:
        return []  
    

    min_element = arr[0]
    max_element = arr[0]
    

    for num in arr[1:]:
        if num < min_element:
            min_element = num
        if num > max_element:
            max_element = num
    
    return [min_element, max_element]

get_min_max([1, 2, 3, 4, 5])
