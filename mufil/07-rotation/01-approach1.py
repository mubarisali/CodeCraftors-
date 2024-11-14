
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
    k = k%len(nums)
    for _ in range(k):
        temp = nums[0]
        for i in range(1,len(nums)):
            temp,nums[i] = nums[i],temp
        nums[0] = temp

        
rotate(nums, 4)
print(nums)
