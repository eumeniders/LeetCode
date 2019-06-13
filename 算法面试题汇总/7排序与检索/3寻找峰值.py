class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp=-2**32+1
        for i in range(len(nums)):
            if i==len(nums)-1:
                if nums[i]>tmp:
                    return i
                else:
                    break
            if nums[i]>tmp and nums[i]>nums[i+1]:
                return i
