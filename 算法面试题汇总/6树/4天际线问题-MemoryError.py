class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        mx = 0
        start,end=min(buildings,key=lambda x:x[0])[0],max(buildings,key=lambda x:x[1])[1]
        h=[0]*(end+1)
        for i in range(start,end+1):
            for x in buildings:
                if x[0]<=i<=x[1]:
                    h[i]=max(h[i],x[2])
        res = []
        tmp = 0
        for i in range(start,end+1):
            if h[i]!=tmp:
                res.append([i,h[i]])
                tmp=h[i]
        return res
