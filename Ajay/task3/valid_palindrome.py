import re

s = "A man, a plan, a canal: Panama"

cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

if cleaned_string == cleaned_string[::-1]:
    print("True")
    
    
#another method
def is_palindrome(s):
    new_s = ''  #new string
    
    for ele in s :
        if ele.isalnum():   #isalnum checks whether the it's an alphanumeric
            new_s += ele.lower()
    
    start , end = 0 ,len(new_s)-1 #two pointers
    
    while start < end : #compare the string from both ends
        if new_s[start] == new_s[end]:
            start += 1
            end -= 1
        else:
            return False
    
    return True  #if everything matched return True

print(is_palindrome(s))    
            
            
    