class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2)!=len(s3):
            return False
        if not s3:
            return True
        elif s1 and s2 and s3[0]==s1[0] and s3[0]==s2[0]:
            return (self.isInterleave(s1[1:],s2,s3[1:]) or self.isInterleave(s1,s2[1:],s3[1:]))
        elif s1 and s3[0]==s1[0]:
            return self.isInterleave(s1[1:],s2,s3[1:])
        elif s2 and s3[0]==s2[0]:
            return self.isInterleave(s1,s2[1:],s3[1:])
        else:
            return False
