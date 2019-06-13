class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0]*len(nums)
        tmp=sorted(nums)
        for i in range(len(nums)):
            tmp.remove(nums[i])
            l,r=0,len(tmp)-1
            while l<=r:
                m=(l+r)/2
                if nums[i]<=tmp[m]:
                    r=m-1
                else:
                    l=m+1
            res[i]=l
        return res
