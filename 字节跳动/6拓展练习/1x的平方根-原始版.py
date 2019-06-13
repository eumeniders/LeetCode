class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x
        l,r=0,x
        while l<=r:
            mid=(l+r)/2
            if mid**2>x and (mid-1)**2<=x:
                return mid-1
            elif mid**2>x:
                r=mid-1
            else:
                l=mid+1
        return l
