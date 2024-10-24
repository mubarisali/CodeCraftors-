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
        
        bin_result = "".join(str(x) for x in result)
        return bin_result