arr = [4,2,5,1000,56,367]
max = arr[0]
min = arr[0]
for i in range (1,len(arr)):
    if arr[i]<min:
        min= arr[i]
    else:
        arr[i]>max
        i=i+1
   
print(max,min)

    