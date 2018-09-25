"""
https://leetcode.com/problems/jump-game/description/
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

"""
class Solution:
    def canJump(self, nums: [int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums: return True
        if len(nums) == 1: return True
        blocked = False
        idx = len(nums) - 2
        while idx >= 0:
            if nums[idx] == 0:
                blocker = idx
                blocked = True
                skip = 1
                for i in range(blocker-1, -1, -1):
                    if (i + nums[i]) > blocker:
                        blocked = False
                        break
                    else: skip +=1
                if blocked: return not blocked
                idx -=skip
            else:
                idx-=1

        return not blocked

#
sol = Solution()
print(sol.canJump([2,3,1,1,4]))

print(sol.canJump([3,2,1,0,4]))





