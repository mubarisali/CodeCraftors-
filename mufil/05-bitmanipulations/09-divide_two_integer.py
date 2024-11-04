#https://leetcode.com/problems/divide-two-integers/

def divide(self, dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    if dividend == -2**31 and divisor == -1:
        return 2**31-1
    if abs(divisor) == 1:
        
        return dividend * divisor

    is_negative = (dividend < 0) ^ (divisor < 0)
    ans = 0

    dividend, divisor = abs(dividend), abs(divisor)

    while (dividend >= divisor):
        i = 0
        while(dividend >= (divisor<<i)):
            i+=1
        i-=1
        ans +=1<<i
        dividend-= divisor<<i

    return -ans if is_negative else ans