class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        num=[]
        for i in range(len(matrix)):
            num+=matrix[i]
        num.sort()
        return num[k-1]
