# Calculate the sum using a while loop break that loop when the user enters 'exit'

# Question
print("Please enter a series of numbers, enter 'exit' to stop:")

# Initialize variables
sum = 0
while True:
    # Get the input from user
    num = input("Enter a number or type exit for getting sum: ")
    
    # Check if user wants to exit
    if num.lower() == "exit":
        break
    
    # Add the number to the sum
    sum += int(num)

# Print the sum
print(f"The sum is: {sum}")
