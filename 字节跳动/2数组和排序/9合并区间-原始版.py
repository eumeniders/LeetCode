class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals[:]=sorted(intervals,key=lambda x:x[0])
        res =[]
        for i in range(len(intervals)):
            if i<len(intervals)-1:
                if intervals[i][1]>=intervals[i+1][0]:
                    tmp = [intervals[i][0],max(intervals[i][1],intervals[i+1][1])]
                    intervals[i+1]=tmp
                else:
                    res.append(intervals[i])
            else:
                res.append(intervals[i])
        return res
