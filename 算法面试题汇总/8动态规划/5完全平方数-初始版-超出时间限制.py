class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        stack=[(n,0)]
        while stack:
            num,step = stack.pop(0)
            i=1
            tnum=num-i**2
            while tnum>=0:
                if tnum==0:
                    return step+1
                stack.append((tnum,step+1))
                i+=1
                tnum=num-i**2
        
