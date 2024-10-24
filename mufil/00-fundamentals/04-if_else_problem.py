def compute_tax(salary):
    """Function to compute tax based on salary."""
    if salary >= 15:
        tax = 30
    elif salary >= 10:
        tax = 20
    elif salary >= 5:
        tax = 10
    else:
        tax = 0
    return tax

def main():
    """Main function to get user input and compute tax."""
    try:
        salary = float(input("Enter your salary: "))
        
        # Compute tax
        tax = compute_tax(salary)

        # Print the result
        print(f"Based on a salary of {salary}, your tax rate is: {tax}%")
        
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Entry point of the program
if __name__ == "__main__":
    main()
