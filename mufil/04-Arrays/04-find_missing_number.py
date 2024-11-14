"""
Given an Array (arr) of size n. It only contains elements from range [1,n].
Return an Array of all integers in the range [1,n] that do not appear in the array.

You Have to solve this question without using any extra array.
Hint:- Try using the last approach of rotate arrays Question

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]

Explanation:- All elements are present from 1 to 8 except 5 and 6.
"""

def missingNumber(nums):
    for ele in nums:
        index = abs(ele) - 1
        if nums[index] > 0:
            nums[index] = -nums[index]
    return [i+1 for i, ele in enumerate(nums) if ele > 0]


print(missingNumber([4,3,2,7,8,2,3,1]))
print(missingNumber([1,1]))
print(missingNumber([1,2,3,4]))