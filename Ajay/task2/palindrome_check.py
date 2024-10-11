
string = input("Enter a string to check whether it's palindrome : ")  
string_lower = string.lower() 


if string_lower == string_lower[::-1]:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
