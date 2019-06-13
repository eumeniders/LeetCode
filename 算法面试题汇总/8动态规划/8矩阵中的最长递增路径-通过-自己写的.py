class Solution(object):
    def long(self,matrix,visit,lex,i,j):
        if visit[i][j]==1:
            return lex[i][j]
        lex[i][j]=1
        visit[i][j]=1
        move = [(1,0),(-1,0),(0,1),(0,-1)]
        for a in range(4):
            x = i+move[a][0]
            y = j+move[a][1]
            if 0<=x<len(matrix) and 0<=y<len(matrix[0]) and matrix[x][y]<matrix[i][j]:
                lex[i][j]=max(lex[i][j],self.long(matrix,visit,lex,x,y)+1)
        return lex[i][j]
            
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        mx = 0
        visit = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        lex   = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mx = max(mx,self.long(matrix,visit,lex,i,j))
        return mx
