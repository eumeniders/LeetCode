class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        for x in nums:
            d[x]=d.get(x,0)+1
        return sorted(d.keys(),key=d.get)[-k:]
