"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Try to Solve in time Complexity 0(n) without any extra Space.
You Dont need to return an Array. Modify array in place. 
"""

nums = [1,3]
k = 2

def rotate(nums, k):
    k = k
    cur_index = 0
    temp = nums[0]
    count = 0
    cycle_position = 0
    while count < len(nums):
        next_index = (cur_index + k) % len(nums)
        temp, nums[next_index] = nums[next_index], temp
        cur_index = next_index
        count += 1
        if (cur_index == cycle_position):
            cur_index = (cur_index + 1) % len(nums)
            cycle_position = cur_index
            temp = nums[cur_index]

rotate(nums, k)
print(nums)