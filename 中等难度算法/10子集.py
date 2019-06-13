class Solution(object):
    def subsets(self, nums):#原版
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = nums
        list = [[]]
        while res:
            temp =[]
            tmp=res.pop()
            for i in range(len(list)):
                temp.append(list[i]+[tmp])
            list+=temp
        return list
    def subsets(self, nums):#精简版
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        list = [[]]
        while nums:
            tmp=nums.pop()
            list+=[x+[tmp] for x in list]
        return list
