class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        nums.sort()
        mx = 1
        tmp = 1
        a = nums[0]+1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            if a==nums[i]:
                tmp+=1
                mx = max(mx,tmp)
                a+=1
            else:
                tmp=1
                a=nums[i]+1
        return mx
