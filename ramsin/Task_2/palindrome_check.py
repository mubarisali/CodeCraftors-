input_string = input("Enter a string or number to check if it's a palindrome: ")  
input_string = input_string.lower().replace(" ","")  


if input_string == input_string[::-1]:
    print(f"{input_string} is a palindrome.")
else:
    print(f"{input_string} is not a palindrome.")



