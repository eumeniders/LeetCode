class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m,n = len(s1)+1,len(s2)+1
        if m+n!=len(s3)+2:
            return False
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if j>0 and dp[i][j-1]==1 and s3[i+j-1]==s2[j-1]:
                    dp[i][j]=1
                if i>0 and dp[i-1][j]==1 and s3[i+j-1]==s1[i-1]:
                    dp[i][j]=1
        return dp[m-1][n-1]==1
        
        
