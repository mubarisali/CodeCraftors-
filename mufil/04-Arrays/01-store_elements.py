# Program to store elements in an array
from array import *

# Ask user for the limit
limit = int(input("Enter a limit : "))

# Initialize an empty array
arr = array('i', [])

# Store elements in the array
for i in range(limit):
    # Ask user for the element
    ele = int(input(f"Enter {i} element : "))
    # Append the element to the array
    arr.append(ele)

# Print the array
print(list(arr))
