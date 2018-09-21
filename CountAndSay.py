"""
https://leetcode.com/problems/count-and-say/description/

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

"""
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        seq = [1]
        while n > 1:
            next = []
            current = seq[0]
            count = 0
            for num in seq:
                if current == num:
                    count +=1
                else:
                    next += [count , current]
                    current = num
                    count = 1
            next += [count, current]
            seq = next
            n = n -1
        return ''.join(str(e) for e in seq)

#
sol = Solution()

for i in range(1,7): print('level %s is %s'% (i, sol.countAndSay(i)))

# print(sol.countAndSay(5))