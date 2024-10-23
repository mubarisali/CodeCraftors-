def find_max(a, b):
    """Function to find the maximum of two numbers."""
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None  # Indicate that both numbers are equal

def main():
    """Main function to get user input and display the largest number."""
    # Get input from the user
    try:
        a = float(input("Enter the first number (a): "))
        b = float(input("Enter the second number (b): "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return  # Exit the program if the input is not valid

    # Find the maximum number
    max_number = find_max(a, b)

    # Print the result
    if max_number is not None:
        print(f"The largest number is: {max_number}")
    else:
        print("Both numbers are equal.")

# Entry point of the program
if __name__ == "__main__":
    main()
