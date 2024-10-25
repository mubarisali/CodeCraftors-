def alternatingBits(num):
    xor =num^(num>>1)
    return(xor &(xor + 1)) ==0
n=67835466
print( alternatingBits(n))