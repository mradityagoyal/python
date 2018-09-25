"""
https://leetcode.com/problems/string-compression/description/

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:
Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
Example 2:
Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
"""
class Solution:
    def compress(self, chars: [str]) -> int:
        """
        :type chars: List[str]
        :rtype: int
        """
        idx = 0

        currentChar = chars[0]
        count = 0
        for i in range(len(chars)):
            nextChar = chars[i]
            if currentChar == nextChar:
                count +=1
            else:
                if count > 1:
                    res = currentChar + str(count)
                    for char in res:
                        chars[idx] = char
                        idx +=1
                else:
                    chars[idx] = currentChar
                    idx +=1
                currentChar= nextChar
                count = 1

        if count > 1:
            res = currentChar + str(count)
            for char in res:
                chars[idx] = char
                idx +=1
        else:
            chars[idx] = currentChar
            idx +=1

        return idx

#
sol = Solution()
# input = ["a","a","b","b","c","c","c"]
# print("compressed length of %r is %s: "%(input, sol.compress(input)))
# print("Residual %r"%input)
#
# input = ["a"]
# print("compressed length of %r is %s: "%(input, sol.compress(input)))
# print("Residual %r"%input)
#
# input = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# print("compressed length of %r is %s: "%(input, sol.compress(input)))
# print("Residual %r"%input)
#
input = ["a","a","a","a","b","a"]
print("compressed length of %r is %s: "%(input, sol.compress(input)))
print("Residual %r"%input)
