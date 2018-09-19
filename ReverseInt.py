# https://leetcode.com/problems/reverse-integer/description/
"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


"""

class ReverseInt:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        if x < 0:
            result= -1* int(str(-1*x)[::-1])
        else: result= int(str(x)[::-1])

        if result < -(2**31) or result > (2**31 -1):
            return 0
        else: return result


ri = ReverseInt()
print(ri.reverse(100))

