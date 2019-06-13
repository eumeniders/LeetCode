class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix==[]:
            return 0
        m,n = len(matrix),len(matrix[0])
        dp = [[0 for x in range(n)] for x in range(m)]
        mx = 0
        for i in range(n):
            dp[0][i]=int(matrix[0][i])
            mx = max(dp[0][i],mx)
        for i in range(m):
            dp[i][0]=int(matrix[i][0])
            mx = max(dp[i][0],mx)
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]=='0':
                    continue
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                mx = max(mx,dp[i][j])
        return mx**2
            
