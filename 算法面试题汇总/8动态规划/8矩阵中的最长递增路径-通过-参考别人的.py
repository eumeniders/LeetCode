class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        maxlen =0
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        def dfs(i,j,m,n):
            if not dp[i][j]:#当之前dfs中，某一个点出发的递增序列得到了，那么在下一轮迭代中，再次经过该节点一样不变，所以这一项就是去重复遍历操作
                tmp = matrix[i][j]
                dp[i][j] = 1+ max(dfs(i+1,j,m,n) if i<m-1 and tmp <matrix[i+1][j]  else 0
                                ,dfs(i-1,j,m,n) if i and tmp <matrix[i-1][j]  else 0
                                ,dfs(i,j+1,m,n) if j<n-1 and tmp<matrix[i][j+1]  else 0 
                                ,dfs(i,j-1,m,n) if j and tmp < matrix[i][j-1]  else 0
                            )
                
            return dp[i][j]
        dp = [[0] * n for i in range(m)]  
        return max(dfs(x, y,m,n) for x in range(m) for y in range(n))
