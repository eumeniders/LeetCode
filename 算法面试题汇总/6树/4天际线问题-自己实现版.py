import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        outline_list=[]
        for left,right,height in buildings:
            outline_list.append([left,-height,right])
            outline_list.append([right,0,0])
        outline_list.sort()
        heap=[[0,float('inf')]]
        result = [[0,0]]
        for left,height,right in outline_list:
            while left>=heap[0][1]:
                heapq.heappop(heap)
            if height!=0:
                heapq.heappush(heap,[height,right])
            if result[-1][1]+heap[0][0]:
                result.append([left,-heap[0][0]])
        return result[1:]
                
