class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==[[]]:
            return False
        for i in range(len(matrix)):
            if target>matrix[i][-1] or target<matrix[i][0]:
                continue
            if target in matrix[i]:
                return True
        return False
        
        
