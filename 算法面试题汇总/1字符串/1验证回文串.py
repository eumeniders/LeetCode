class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        val ='0123456789abcdefghijklmnopqrstuvwxyz'
        tmp = ''
        for x in s:
            if x in val:
                tmp+=x
        s=tmp
        l,r=0,len(s)-1
        while l<r:
            print s[l],s[r]
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return False
        return True
