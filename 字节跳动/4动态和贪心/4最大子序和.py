class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = nums[0]
        sm = nums[0]
        for i in range(1,len(nums)):
            if sm<0:
                sm = nums[i]
            else:
                sm += nums[i]
            mx = max(mx,sm)
        return mx
