class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l,r,o=1,1,[1]*n
        for i in range(n):
            o[i]*=l
            o[n-i-1]*=r
            l*=nums[i]
            r*=nums[n-i-1]
        return o
        
