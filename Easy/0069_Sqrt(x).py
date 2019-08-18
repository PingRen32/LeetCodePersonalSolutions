# Implement int sqrt(int x).
#
# Compute and return the square root of x,
# where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer,
# the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x < 3:
            return 1
        # Babylonian method
        size = len(str(x))
        res = size * 10**size
        while True:
            per = (res + x / res) / 2
            if int(per) == int(res):
                return int(res)
            else:
                res = per