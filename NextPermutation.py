class NextPermutation:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2: return

        for i in range(len(nums)-1, 0, -1):
            prev = i -1
            if nums[i] > nums[i-1]:
                # find the first num larger than nums[i-i] in nums[last] to nums[i]
                idNextLarger = -1
                for idx in range(len(nums)-1, i-1, -1):
                    if nums[idx] > nums[i-1]:
                        idNextLarger = idx
                        break
                #swap i-1 and idNextLarger
                self.swap(nums, i-1, idNextLarger)
                #reverse the list from i to the end.
                self.reverse(nums, i)
                return

        # all are ascending. reverse these.
        for i in range(0, int(len(nums)/2)):
            last = len(nums) -1
            self.swap(nums, i, last -i)


    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i]=nums[j]
        nums[j]=temp

    def reverse(self, nums, startIdx):
        """
        reverse the nums from start idx. in place.
        :param nums:
        :param startIdx:
        :return:
        """
        for i in range(0, int((len(nums)-startIdx)/2)):
            self.swap(nums, startIdx+i , len(nums)-1 - i)

# startup
np = NextPermutation()
nums = [2,3,1]
np.nextPermutation(nums)
print(nums)