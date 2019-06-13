class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        mas = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    continue
                num = 0
                land = [(i,j)]
                while land:
                    r,n =land.pop()
                    if grid[r][n]==0:
                        continue
                    grid[r][n]=0
                    num+=1
                    if r>0 and grid[r-1][n]==1:
                        land.append((r-1,n))
                    if r<len(grid)-1 and grid[r+1][n]==1:
                        land.append((r+1,n))
                    if n>0 and grid[r][n-1]==1:
                        land.append((r,n-1))
                    if n<len(grid[0])-1 and grid[r][n+1]==1:
                        land.append((r,n+1))
                    mas = max(mas,num)
        return mas
                        
