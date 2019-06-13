class Solution(object):
    def __init__(self):
        self.mx=1
    def long(self,matrix,i,j,res):
        if i<0 or i>=len(matrix) or j<0 or j>=len(matrix[0]) or matrix[i][j]<=res[-1]:
            self.mx = max(self.mx,len(res))
            return self.mx
        tmp = matrix[i][j]
        matrix[i][j]=float('-inf')
        self.long(matrix,i-1,j,res+[tmp])
        self.long(matrix,i+1,j,res+[tmp])
        self.long(matrix,i,j-1,res+[tmp])
        self.long(matrix,i,j+1,res+[tmp])
        matrix[i][j]=tmp
        
            
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.long(matrix,i,j,[-1])
        return self.mx-1
