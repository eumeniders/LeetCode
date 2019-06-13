class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for x in nums:
            d[x]=d.get(x,0)+1
            if d[x]>len(nums)/2:
                return x
