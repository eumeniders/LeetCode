class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1,d2={},{}
        for x in s:
            d1[x]=d1.get(x,0)+1
        for y in t:
            d2[y]=d2.get(y,0)+1
        if d1==d2:
            return True
        return False
