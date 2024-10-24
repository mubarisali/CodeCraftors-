# 4.https://www.geeksforgeeks.org/problems/string-functions-i/1

def trim(str):
    # Use strip() to remove leading and trailing spaces
    return str.strip()

def exists(str, x):
    # Use find() to check if x exists in str, returns -1 if not found
    return str.find(x)

def titleIt(str):
    # Use title() to capitalize the first letter of each word
    return str.title()

def casesSwap(str):
    # Use swapcase() to swap case of each character
    return str.swapcase()
