class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height==[]:
            return 0
        idx = height.index(max(height))
        l,r = 0,len(height)-1
        lh,rh = 0,0
        res =0
        while l<idx:
            lh=max(lh,height[l])
            res += lh-height[l]
            l+=1
        while r>idx:
            rh=max(rh,height[r])
            res += rh-height[r]
            r-=1
        return res
