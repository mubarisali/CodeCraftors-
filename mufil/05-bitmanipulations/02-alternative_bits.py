# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/

#1010101010

def has_alternating_bits(n):
    first_bit = n & 1
    n = n >> 1

    while n > 0:
        second_bit = n & 1
        if second_bit == first_bit:
            return False
        first_bit = second_bit
        n = n >> 1

    return True
print(has_alternating_bits(699050), bin(699050)[2:])
print(has_alternating_bits(11) , bin(11)[2:])



        