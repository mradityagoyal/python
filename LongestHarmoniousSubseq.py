# https://leetcode.com/problems/longest-harmonious-subsequence/description/
class LongestHarmoniousSubseq(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        d = collections.Counter(nums)
        result = 0
        for (key, val) in d.items():
            if key + 1 in d :
                result = max(result, val + d[key+1])
        return result

# default run

lhs = LongestHarmoniousSubseq()
print(lhs.findLHS([1,2,1,1,2,3,3,3,4,4,4,4,4,4,2,2,2]))
print(lhs.findLHS([]))
print(lhs.findLHS([1,1,1,3,3,3,3,3,3,3,33]))