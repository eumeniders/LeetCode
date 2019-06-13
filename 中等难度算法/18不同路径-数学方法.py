class Solution(object):
    def jiecheng(self,m):
        if m==0 or m==1:
            return 1
        else:
            return m*self.jiecheng(m-1)
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.jiecheng(m+n-2)/self.jiecheng(max(m-1,n-1))/self.jiecheng(min(m-1,n-1))
