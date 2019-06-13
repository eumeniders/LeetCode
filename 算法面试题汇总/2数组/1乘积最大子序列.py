class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp1=[nums[0]]*len(nums)
        dp2=[nums[0]]*len(nums)
        for i in range(1,len(nums)):
            dp1[i]=max(dp1[i-1]*nums[i],dp2[i-1]*nums[i],nums[i])
            dp2[i]=min(dp2[i-1]*nums[i],dp1[i-1]*nums[i],nums[i])
        return max(dp1)
