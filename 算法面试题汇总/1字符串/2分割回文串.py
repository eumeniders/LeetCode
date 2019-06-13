class Solution:
    def ishw(self,s):
        l,r=0,len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
    def part(self,res, l, r):
        print l,r
        if len(r) == 0:
            res.append(l[:])
            return 
        for i in range(len(r)):
            if self.ishw(r[:i+1]):
                l.append(r[:i+1])
                self.part(res, l, r[i+1:])
                l.pop()
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.part(res,[], s)
        return res
