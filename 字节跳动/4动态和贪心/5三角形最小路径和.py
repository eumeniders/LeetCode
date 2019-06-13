class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        l = len(triangle)
        dp = [[0 for i in range(x)] for x in range(1,l+1)]
        dp[0][0]=triangle[0][0]
        for i in range(1,l):
            dp[i][0]=dp[i-1][0]+triangle[i][0]
            dp[i][i]=dp[i-1][i-1]+triangle[i][i]
        for i in range(1,l):
            for j in range(1,i):
                dp[i][j]=min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]
        return min(dp[l-1])
