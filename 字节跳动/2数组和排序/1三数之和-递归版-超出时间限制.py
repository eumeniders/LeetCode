class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        dic_l = []
        def isval(s):
            if sum(s)==0:
                if s not in res:
                    d = {}
                    for x in s:
                        d[x]=d.get(x,0)+1
                    if d not in dic_l:
                        return True
            return False
        def dfs(a,nums,k):
            if k==3:
                if isval(a):
                    d = {}
                    for x in a:
                        d[x]=d.get(x,0)+1
                    dic_l.append(d)
                    res.append(a)
                return
            else:
                for i in range(len(nums)):
                    dfs(a+[nums[i]],nums[:i]+nums[i+1:],k+1)
        dfs([],nums,0)
        return res
