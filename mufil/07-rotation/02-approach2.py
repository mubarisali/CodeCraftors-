"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Try to Solve in time Complexity 0(n) with extra Space.
"""

nums = [1,2,3,4,5,6,7]
k = 3

def rotate(nums, k):
    result = [0]*len(nums)
    for i in range(len(nums)):
        result[(i+k)%len(nums)] = nums[i]
    return result
    
print(rotate(nums, k))