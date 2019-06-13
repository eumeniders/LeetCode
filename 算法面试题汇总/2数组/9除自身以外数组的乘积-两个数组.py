class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l,r,o=[1]*n,[1]*n,[1]*n
        l[0],r[n-1]=nums[0],nums[n-1]
        for i in range(1,len(nums)):
            l[i]=l[i-1]*nums[i]
            r[n-1-i]=r[n-i]*nums[n-i-1]
        o[0],o[n-1]=r[1],l[n-2]
        for i in range(1,n-1):
            o[i]=l[i-1]*r[i+1]
        return o
        
