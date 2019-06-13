class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = [] 
        def isval(s):
            a = int(s)
            if 0<=a<=255 and (len(s)==1 or s[0]!='0'):
                return True
            return False
        def dfs(a,s,k):
            if k==3:
                if isval(s):
                    res.append(a+s)
                return
            else:
                for i in range(1,min(4,len(s))):
                    tmp=s[:i]
                    if isval(tmp):
                        dfs(a+tmp+'.',s[i:],k+1)
        dfs('',s,0)
        return res
