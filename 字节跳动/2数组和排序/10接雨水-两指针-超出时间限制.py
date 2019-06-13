class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,2
        res = 0
        le = len(height)
        while l<le-2 and r<le:
            if height[l+1]>=height[l]:
                l+=1
                r+=1
                continue
            if height[r]>=height[l]:
                tmp = (r-l-1)*height[l]-sum(height[l+1:r])
                if tmp>0:
                    res +=tmp
                l,r = r,r+2
            else:
                lef = height[l+1:]
                mx = max(lef)
                if mx>=height[l]:
                    r+=1
                    continue
                else:
                    lef = lef[::-1]
                    idx = lef.index(mx)
                    r = le-idx-1
                    tmp = (r-l-1)*height[r]-sum(height[l+1:r])
                    res+=tmp
                    l = r
                    r +=2
        return res
height=[6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
a=Solution()
print a.trap(height)
