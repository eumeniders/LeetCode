class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>res[-1]:
                res.append(nums[i])
            else:
                l,r=0,len(res)-1
                while l<=r:
                    mid=(l+r)//2
                    if nums[i]>res[mid]:
                        l=mid+1
                    else:
                        r=mid-1
                res[l]=nums[i]
        return len(res)
                        
