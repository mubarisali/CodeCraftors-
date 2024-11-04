numbers = [10,16,22,35,48,56,78,89,99,100,121,136,154,178,189,199]

search = 10

low = 0
high = len(numbers)-1

while low <= high :
    mid = (low + high) //2
    
    if numbers[mid] == search :
        print( f"Element found at index {mid}")
        break
    elif numbers[mid] < search:
        low = mid + 1
    else:
        high = mid - 1
else :
    print("Element not found!")