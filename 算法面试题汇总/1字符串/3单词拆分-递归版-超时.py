class Solution(object):
    def word(self,r,start,wordDict):
        if len(r)==0:
            return True
        for i in range(start,len(r)):
            if r[:i+1] in wordDict:
                return self.word(r[i+1:],0,wordDict) or self.word(r,i+1,wordDict)
        return False
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        return self.word(s,0,wordDict)
