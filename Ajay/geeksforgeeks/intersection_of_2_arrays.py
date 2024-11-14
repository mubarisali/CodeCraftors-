arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 6, 7, 8]

ans=[]
for num in arr1:
    if num in arr2 and num not in ans:
        ans.append(num)
        arr2.remove(num)
        
print(ans)

#another way
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 6, 7, 8]

set1 = set(arr1)
set2 = set(arr2)

print(sorted(list(set1.intersection(set2))))