"""
https://leetcode.com/problems/majority-element-ii/description/
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

"""
import collections
class MajorityElement2:
    def majorityElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [num
                for num, ct in collections.Counter(nums).items()
                if ct > int(len(nums) / 3)]

nums = ['a','b','b','c']
print(list(collections.Counter(nums)))
me = MajorityElement2()
me.majorityElement2([3,2,3])


"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

"""
def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for num , count in collections.Counter(nums).items():
        if count > len(nums)/2: return num

