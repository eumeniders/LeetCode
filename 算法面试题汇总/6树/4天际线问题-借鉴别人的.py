import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # 只需比较每栋建筑的左右两边，是否需要记录即可
        path = []
        for l, r, h in buildings:
            path.append((l, - h, r))
            path.append((r, 0, 0))
        
        # 保证从左向右，且相同横坐标最高的先被访问
        path = sorted(path)
        # print path
        
        # 高度与右边界的最小堆，保证实际高度最大的在最前面
        hi_q = [(0, float('inf'))]
        
        # 目标结果集，初始化一个元素为了方便 result[-1] 获取
        result = [[0, 0]]
        for x, neg_h, r in path:
            # 如果最高点已在当前点的左侧，说明需要过期处理
            while hi_q[0][1] <= x:
                heapq.heappop(hi_q)
            
            # 如果是左侧节点（右侧节点 neg_h==0）
            if neg_h:
                heapq.heappush(hi_q, [neg_h, r])
                
            if result[-1][1] + hi_q[0][0]:
                result.append([x, - hi_q[0][0]])
        return result[1:]
                
