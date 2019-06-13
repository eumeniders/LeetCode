class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        l = len(M)
        yl = []
        for i in range(l):
            yl.append(i)
        tl = []
        f = 0
        while yl:
            if tl==[]:
                f +=1
                tl.append(yl.pop(0))
            while tl:
                tmp = tl.pop(0)
                for i in range(l):
                    if M[tmp][i]==1 and i in yl:
                        tl.append(i)
                        yl.remove(i)
        return f
M=[[1,1,0],[1,1,0],[0,0,1]]
a = Solution()
print a.findCircleNum(M)
