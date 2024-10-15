
arr = [1 ,10 ,22, 45, 67 ,998 , 23 , 34 ,55]

min_val = max_val = arr[0]

for num in arr :
    if num < min_val:
        min_val = num
    elif num > max_val:
        max_val = num
        
print(f"{min_val} , {max_val}")
