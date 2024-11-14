def sum_of_natural_numbers():
    # Prompt the user for the value of n
    n = int(input("Enter a positive integer n: "))
    
    if n < 0:
        print("Please enter a positive integer.")
    else:
        # Calculate the sum using a loop
        total_sum = 0
        for i in range(1, n + 1):
            total_sum += i
        
        # Print the result
        print(f"The sum of all natural numbers up to {n} is: {total_sum}")

# Run the function
sum_of_natural_numbers()
