class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n==1:
            return '1'
        num = '123456789'
        num = num[:n]
        jcl = [0,1]
        res = []
        for i in range(2,n):
            jcl += [jcl[i-1]*i]
        while k:
            while jcl:
                tmp = jcl.pop()
                if tmp==0:
                    res.append(num[0])
                    k=0
                    break
                if k%tmp!=0:
                    res.append(num[k/tmp])
                    num = num[:k/tmp]+num[k/tmp+1:]
                    k = k%tmp
                if k%tmp==0:
                    res.append(num[k/tmp-1])
                    num = num[:k/tmp-1]+num[k/tmp:]
                    k=tmp
        return ''.join([str(x) for x in res])
