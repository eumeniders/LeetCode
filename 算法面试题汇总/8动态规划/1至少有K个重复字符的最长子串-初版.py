class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        d={}
        for x in s:
            d[x]=d.get(x,0)+1
        for x in d:
            if d[x]<k:
                idx = s.index(x)
                return max(self.longestSubstring(s[:idx],k),self.longestSubstring(s[idx+1:],k))
        return len(s)
        
