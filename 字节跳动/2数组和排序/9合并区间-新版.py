class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        i = 0
        while i<len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0]:
                intervals=intervals[:i]+[[min(intervals[i][0],intervals[i+1][0]),max(intervals[i][1],intervals[i+1][1])]]+intervals[i+2:]
            else:
                i+=1
        return intervals
a = Solution()
intervals = [[1,4],[0,0]]
print a.merge(intervals)
