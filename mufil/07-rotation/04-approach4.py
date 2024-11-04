"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

"""

nums = [1,2,3,4,5,6,7]
k = 3

def rotate(nums, k):
    k = k % len(nums) 
    return  nums[-k:] + nums[:-k]



print(rotate(nums, k))