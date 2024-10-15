user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0

# Correct indentation for the loop
for char in user_input:
    if char in vowels:
        vowel_count += 1

# Print the result after the loop
print(f"The total number of vowels in the string is: {vowel_count}")
