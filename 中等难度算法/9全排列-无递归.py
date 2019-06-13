class Solution(object):
    def perm(self,nums):
        res = []
        while nums:
            tmp = nums.pop()
            if res==[]:
                res.append([tmp])
            else:
                l_tmp=[]
                for i in range(len(res)):
                    for j in range(len(res[i])+1):
                        l_tmp.append(res[i][:j]+[tmp]+res[i][j:])
                res = l_tmp
        return res

            
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.perm(nums)
