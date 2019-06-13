class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic ={}
        for x in nums:
            dic[x]=dic.get(x,0)+1
        if target not in dic.keys():
            return [-1,-1]
        else:
            start_index=nums.index(target)
            end_index=start_index+dic.get(target)-1
            return [start_index,end_index]
