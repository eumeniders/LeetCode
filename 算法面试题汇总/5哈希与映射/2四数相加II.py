class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        l = len(A)
        d={}
        res=0
        for i in range(l):
            for j in range(l):
                d[A[i]+B[j]]=d.get(A[i]+B[j],0)+1
        for i in range(l):
            for j in range(l):
                res+=d.get(-C[i]-D[j],0)
        return res
