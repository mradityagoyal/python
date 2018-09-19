"""
https://leetcode.com/problems/reordered-power-of-2/description/
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.



Example 1:

Input: 1
Output: true
Example 2:

Input: 10
Output: false
Example 3:

Input: 16
Output: true
Example 4:

Input: 24
Output: false
Example 5:

Input: 46
Output: true
"""

class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        powers = []
        current = 1
        # dont need to create all the powers.
        #just create powers upto 10^ lengthofN or max N = 10^9
        maxPow = 10**min(len(str(N)), 9)
        while(current <= maxPow):
            powers.append(current)
            current*=2

        import collections
        counters = [collections.Counter(str(power)) for power in powers]

        counterN = collections.Counter(str(N))

        if counterN in counters : return True
        else: return False
