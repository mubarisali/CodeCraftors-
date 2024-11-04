
"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Try to Solve in time Complexity 0(n*k).
You Dont need to return an Array. Modify array in place. 
"""


nums = [1,2,3,4,5,6,7]
k = 1

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    for _ in range(k):
        val = nums[0]
        for j in range(1,len(nums)):
            temp = nums[j]
            nums[j] = val
            val = temp
        nums[0] = val

        
rotate(nums, 4)
print(nums)
