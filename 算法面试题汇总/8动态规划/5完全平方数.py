class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        q = [[n, 0]]
        visited = [False for _ in range(n + 1)]
        visited[n] = True
        while any(q):
            num, step = q.pop(0)   # 出栈，被pop掉的元素将同时返回给两个变量
            i = 1
            tnum = num - i ** 2
            while tnum >= 0:            # 前进一步
                if tnum == 0: return step + 1   # 最先到达0的一定是步数最少的
                if not visited[tnum]:
                    q.append((tnum, step + 1))
                    visited[tnum] = True     # 只添加没有遍历过的节点，减少计算量
                i += 1
                tnum = num - i ** 2

                
        
