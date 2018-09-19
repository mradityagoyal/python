# https://leetcode.com/problems/letter-case-permutation/description/
"""
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length at most 12.
S will consist only of letters or digits.
"""
class LetterCasePermutation:
    def letterCasePermutation(self, S:str) -> [str]:
        """
        :type S: str
        :rtype: List[str]
        """
        def helper(acc: [str], s: str)-> [str] :
            if not s: return acc
            if s[0].lower() == s[0].upper():
                if not acc:
                    acc.append(s[0])
                else:
                    acc = [item+ s[0] for item in acc]
            else:
                if not acc:
                    acc.append(s[0].lower())
                    acc.append(s[0].upper())
                else:
                    acc = [item+ s[0].lower() for item in acc] + [item + s[0].upper() for item in acc]
            return helper(acc, s[1:])
        return helper([""], S)

#
lcp = LetterCasePermutation()
print(lcp.letterCasePermutation("a1b2"))
print(lcp.letterCasePermutation("3z4"))