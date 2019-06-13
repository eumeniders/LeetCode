class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        res = []
        tmp = '0'
        l,r=(len(nums)-1)/2,len(nums)-1
        while l>=0:
            res.append(nums[l])
            if r>(len(nums)-1)/2:
                res.append(nums[r])
            l-=1
            r-=1
        nums[:]=res
