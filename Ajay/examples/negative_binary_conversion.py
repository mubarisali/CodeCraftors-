num = int(input("Enter a number to convert it into binary form : "))

def binary_representor(num):
    
    if num == 0:
        return "0" * 8  

    
    nums = abs(num)
    binary = ""
    while nums > 0:
        bit = nums % 2
        binary = str(bit) + binary
        nums = nums // 2

    
    binary = binary.zfill(8)

    
    if num > 0:
        return binary

    
    inverted_binary = ""
    for bit in binary:
        inverted_binary += '1' if bit == '0' else '0'

   
    carry = 1
    two_complement = ""
    for bit in inverted_binary[::-1]:  
        if bit == '1' and carry == 1:
            two_complement = '0' + two_complement
        elif bit == '0' and carry == 1:
            two_complement = '1' + two_complement
            carry = 0
        else:
            two_complement = bit + two_complement

    
    if carry == 1:
        two_complement = '1' + two_complement

    
    return two_complement.zfill(8)

print(binary_representor(num))
