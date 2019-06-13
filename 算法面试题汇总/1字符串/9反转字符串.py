class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        l,r=0,len(s)-1
        while l<r:
            tmp=s[l]
            s[l]=s[r]
            s[r]=tmp
            l+=1
            r-=1
