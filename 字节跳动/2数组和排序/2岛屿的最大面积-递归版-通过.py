class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        l = len(nums)
        for i in xrange(l):
            if nums[i]>0:
                break
            if i>=1 and nums[i]==nums[i-1]:
                continue
            j,k= i+1,l-1
            while j<k:
                tmp = nums[i]+nums[j]+nums[k]
                if tmp==0:
                    res.append([nums[i]]+[nums[j]]+[nums[k]])
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j+=1
                    k-=1
                elif tmp>0:
                    k-=1
                else:
                    j+=1
        return res
