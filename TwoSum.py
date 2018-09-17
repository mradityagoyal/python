# https://leetcode.com/problems/two-sum/description/

class TwoSum(object):
    def twoSum(self, nums, target):
        # in a loop.. start creating a map.. key = num, value = index.
        #check if (target - num) is in map... return
        d = {}
        for idx, val in enumerate(nums):
            if (target - val) in d:
                return [idx, d[target-val]]
            else: d[val] = idx

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """