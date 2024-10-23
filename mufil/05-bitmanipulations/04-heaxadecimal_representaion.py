# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/


def toHex(num):
    hexas = "0123456789abcdef"
    
    if num == 0:
        return "0"
    
    if num > 0 and num <= 15:
        return hexas[num]
    
    if num > 0:
        result = ""
        while num > 0:
            result = hexas[num % 16] + result
            num //= 16
        return result
    
    if num < 0:
        num = abs(num)
        result = [0] * 8 
        i = 7
        while num > 0:
            result[i] = num % 16
            num //= 16
            i -= 1
        
        for i in range(8):
            result[i] = 15 - result[i]
        
        carry = 1
        for i in range(7, -1, -1):
            result[i] += carry
            if result[i] == 16:
                result[i] = 0
                carry = 1
            else:
                carry = 0
        
        hex_result = "".join(hexas[d] for d in result)
        return hex_result