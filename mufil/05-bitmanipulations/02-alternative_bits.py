# Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/


def has_alternating_bits(n):
    has_alternating_bits = True
    first_bit = n & 1
    n = n >> 1

    while n > 0:
        second_bit = n & 1
        if second_bit == first_bit:
            has_alternating_bits = False
            break
        first_bit = second_bit
        n = n >> 1

    return has_alternating_bits

print(has_alternating_bits(699050))
print(has_alternating_bits(11))



        