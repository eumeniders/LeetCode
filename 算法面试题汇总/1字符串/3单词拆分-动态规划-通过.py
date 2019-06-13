class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp=[0]*len(s)
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[i]=1
            for j in range(i):
                if dp[j]==1 and s[j+1:i+1] in wordDict:
                    dp[i]=1
        return dp[-1]
