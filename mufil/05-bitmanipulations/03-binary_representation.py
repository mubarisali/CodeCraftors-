"""
Given a 32-bit integer num, return a string representing its binary representation. For negative integers, the two’s complement method should be used.

All the digits in the answer string should be in lowercase characters ('0' or '1'), and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.
"""


def toBinary(num):
    if num == 0:
        return "0"
    if num > 0:
        result = ""
        while num > 0:
            result = str(num % 2) + result
            num //= 2
        return result
    
    if num < 0:
        num = abs(num)
        result = [0] * 32 
        i = 31
        while num > 0:
            result[i] = num % 2
            num //= 2
            i -= 1
        
        for i in range(32):
            result[i] = 1 - result[i]
        
        carry = 1
        for i in range(31, -1, -1):
            result[i] += carry
            if result[i] == 2:
                result[i] = 0
                carry = 1
            else:
                carry = 0
                break
        
        bin_result = "".join(str(x) for x in result)
        return bin_result
    
print(toBinary(-1))