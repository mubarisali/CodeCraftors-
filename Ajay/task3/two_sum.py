def two_sum(nums):
    hashMap = {}
    i = 0
    
    while i < len(nums):
        
        value = target - nums[i]
        
        if value not in hashMap:
            hashMap[nums[i]] = i
            i += 1
        else:
            return [hashMap[value] , i]



nums = [2,1,5,3]
target = 4

result = two_sum(nums)
print(result)