class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        q = collections.deque()
        dx = [-1,1,0,0]
        dy = [0,0,-1,1] 
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append([i,j])
                    grid[i][j] = 0
                    val = 1
                    while len(q) != 0:
                        dd = q.popleft()
                        x = dd[0]
                        y = dd[1]
                        for p in range(4):
                            xx = x+dx[p]
                            yy = y+dy[p]
                            if xx > -1 and xx < n and yy > -1 and yy < m and grid[xx][yy] == 1:
                                val+=1
                                q.append([xx,yy])
                                grid[xx][yy] = 0
                    ans  = max(ans,val)
        return ans