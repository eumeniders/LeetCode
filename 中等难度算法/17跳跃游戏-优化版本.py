class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        far = nums[0]
        for i in range(len(nums)):
            if i <=far:
                far=max(far,i+nums[i])
            if far >=len(nums)-1:
                return True
        return False
