class Solution(object):
    def __init__(self):
        self.mx=0
    def long(self,matrix,i,j,res):
        if 0<=i<len(matrix) and 0<=j<len(matrix[0]) and matrix[i][j]>res[-1]:
            tmp = matrix[i][j]
            matrix[i][j]=0
            self.mx = max(self.mx,self.long(matrix,i+1,j,res+[tmp]),self.long(matrix,i-1,j,res+[tmp]),self.long(matrix,i,j+1,res+[tmp]),self.long(matrix,i,j-1,res+[tmp]))
            matrix[i][j]=tmp
            return self.mx
        else:
            return len(res)
            
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
