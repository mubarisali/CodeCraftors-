"""
Given a String Extract all numbers from it and store it inside an array. Return the Array Once extraction is completed.
Note that if the string is "abc334vf" then the number is 334 and not 3,3,4 as individual numbers

Example 1:
Input:
str = "abc334v44d"
Output: [334, 44]

Example 2:
Input:
str = "abv345fjjf123tyir45jf6th"
Output: [345, 123, 45, 6]

Example 3:
Input:
str = "12jgskjh3shjy355ghgf2673ygs001ghhg9876"
output: [12, 3, 355, 267, 001, 9876]

Constraints:
1 ≤ |str| ≤ 10^4
str contains only alphabets and digits.
"""

def extract_numbers(str):
    num = []
    current_num = ""
    for ele in str:
        if ele.isdigit():  # if (ord(ele) - ord('0') >= 0 and ord(ele) - ord('0') <= 9):
            current_num += ele
        else:
            if current_num:
                num.append(int(current_num))
                current_num = ""
    if current_num:
        num.append(int(current_num))

    return num

print(extract_numbers("abc334v44d"))
print(extract_numbers("abv345fjjf123tyir45jf6th"))
print(extract_numbers("12jgskjh3shjy355ghgf2673ygs001ghhg9876"))

