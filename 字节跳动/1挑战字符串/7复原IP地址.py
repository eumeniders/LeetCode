class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        lst=0
        ans = []
        t = ''
        def isvalid(s):
            a = int(s)
            if (0<=a<=255 and s[0]!='0') or len(s)==1:
                return True
            else:
                return False
        def findip(ans,t,s,lst):
            if lst ==3:
                if isvalid(s):
                    ans.append(t+s)
                return ans
            else:
                for j in range(1,min(4,len(s))):
                    tmp = s[:j]
                    if isvalid(tmp):
                        findip(ans,t+tmp+'.',s[j:],lst+1)
        findip(ans,t,s,lst)
        return ans
