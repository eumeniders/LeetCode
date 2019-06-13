class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d1= {}
        for x in s1:
            d1[x]=d1.get(x,0)+1
        l1 = len(s1)
        l2 = len(s2)
        d2 = {}
        for x in s2[:l1]:
            d2[x]=d2.get(x,0)+1
        if d2==d1:
            return True
        else:
            for i in xrange(l2-l1):
                d2[s2[i]]=d2.get(s2[i])-1
                if d2.get(s2[i])==0:
                    d2.pop(s2[i])
                d2[s2[i+l1]]=d2.get(s2[i+l1],0)+1
                if d1==d2:
                    return True
        return False
