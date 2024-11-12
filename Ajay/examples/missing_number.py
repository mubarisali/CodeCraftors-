#missing number my solution

nums = [1,2,3,5]

length = len(nums)
for i in range(1, length + 2):
    nums.append(i)

print(nums)

nums = [num for num in nums if nums.count(num) == 1]

print(nums)