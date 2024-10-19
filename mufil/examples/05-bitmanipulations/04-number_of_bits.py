#Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).
#https://leetcode.com/problems/number-of-1-bits/description/
num = 2147483645
def count_set_bits(num):
    count = 0
    while num:
        count += num & 1
        num = num >> 1
    return count

print(count_set_bits(num))