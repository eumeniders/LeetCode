class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        num = []
        for i in xrange(1,n+1):
            num+=[i]
        res = [num[0]]
        a = num[1:]
        while a:
            x = a.pop(0)
            tmp = []
            while res:
                y = res.pop(0)
                if y ==1:
                    y=[1]
                for i in range(len(y)+1):
                    tmp.append(y[:i]+[x]+y[i:])
            res = tmp
        return ''.join(str(x) for x in sorted(res)[k-1])
a = Solution()
print a.getPermutation(9,94626)
