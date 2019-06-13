class Solution(object):
    def word(self,res,l,r,wordDict):
        if len(r)==0:
            res.append(' '.join(l[:]))
        for i in range(len(r)):
            if r[:i+1] in wordDict:
                l.append(r[:i+1])
                self.word(res,l,r[i+1:],wordDict)
                l.pop()
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        res = []
        dp=[0]*len(s)
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                dp[i]=1
            for j in range(i+1):
                if dp[j]==1 and s[j+1:i+1] in wordDict:
                    dp[i]=1
        if dp[-1]==1:
            self.word(res,[],s,wordDict)
        return res
其实就是把单词划分的动态规划和递归合并使用
