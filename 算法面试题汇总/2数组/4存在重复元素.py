class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        for x in nums:
            d[x]=d.get(x,0)+1
            if d.get(x)>1:
                return True
        return False
