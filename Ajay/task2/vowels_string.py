name = input("Enter a String : ")
vowel_count = 0

for letter in name :
    if letter == 'a' or letter =='A':
        vowel_count+=1
    elif letter == 'e' or letter =='E':
        vowel_count+=1
    elif letter == 'i' or letter =='I':
        vowel_count+=1
    elif letter == 'o' or letter =='O':
        vowel_count+=1
    elif letter == 'u' or letter =='U':
        vowel_count+=1

print(f"Number of vowels in the string is {vowel_count}")