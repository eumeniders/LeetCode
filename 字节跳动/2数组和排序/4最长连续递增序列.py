class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = 1
        if nums==[]:
            return 0
        tmp = [nums[0]]
        for i in xrange(1,len(nums)):
            if nums[i]>tmp[-1]:
                tmp+=[nums[i]]
                mx = max(mx,len(tmp))
            else:
                tmp=[nums[i]]
        return mx
