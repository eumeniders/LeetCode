class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        tmp = ''
        for i in range(len(s)):
            print s[i]
            if i==len(s)-1 and s[i]!=' ':
                tmp+=s[i]
                res.append(tmp)
            elif s[i]!=' ':
                tmp+=s[i]
            else:
                if tmp!='':
                    res.append(tmp)
                tmp = ''
        re = ''
        while res:
            tmp = res.pop()
            re += tmp+' '
        return re[:-1]
