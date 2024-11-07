
"""
You have given a string , You have to add characters at start of string to make it a palindrome .
return the minimum number of characters required to add to make it a palindrome.

Example 1:
Input:
str = "abcd"
Output: 3
Explanation: We need to add "dcb" at the start of string to make it a palindrome.

Example 2:
Input:
str = "aa"
Output: 0
Explanation:"aa" is already a palindrome.



Constraints:
1 ≤ |str| ≤ 10^3
str contains only lower case alphabets.
"""

#solution 1 

def minInsertions1(s):
    for i in range(len(s)):
        if(isPalindrome(s[:len(s) - i])):
            return i
    return len(s)
def isPalindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True

print(minInsertions1("abacada"))
print(minInsertions1("a"))
print(minInsertions1("malayalam"))
print(minInsertions1("racecar"))
print(minInsertions1("banana"))


#Solution2
def minInsertions2(s):
    start = 0 
    end = len(s) - 1
    pointer = end
    while(start<end):
        if(s[start]==s[end]):
            start+=1
            end-=1
        else:
            start = 0
            pointer -=1
            end = pointer
    return len(s)-pointer-1

# print(minInsertions2("abacada"))
# print(minInsertions2("a"))
# print(minInsertions2("malayalam"))