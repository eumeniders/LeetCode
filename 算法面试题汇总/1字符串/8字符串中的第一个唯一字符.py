class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        mi=len(s)
        for x in s:
            d[x]=d.get(x,0)+1
        for y in d:
            if d[y]==1:
                mi=min(mi,s.index(y))
        if mi!=len(s):
            return mi
        return -1
        
        
