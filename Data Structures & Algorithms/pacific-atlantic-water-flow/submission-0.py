class Solution:
    def pacificAtlantic(self, grid: list[list[int]]) -> list[list[int]]:
        n = len(grid)
        m = len(grid[0])
        q1 = deque()
        q2 = deque()
        dx = [0,0,-1,1]
        dy = [1,-1,0,0]
        v1 = [[False] * m for _ in range(n)]
        v2 = [[False] * m for _ in range(n)]
       
        for i in range(m):
            q1.append([0,i])
            q2.append([n-1,i])
            v1[0][i] = True
            v2[n-1][i] = True

        for i in range(n):
            q1.append([i,0])
            q2.append([i,m-1])
            v1[i][0] = True
            v2[i][m-1] = True
        ans = []
        while q1:
            x,y = q1.popleft()
            for k in range(4):
                xx = x+dx[k]
                yy = y+dy[k]
                if xx > -1 and yy > -1 and xx < n and yy < m and not v1[xx][yy] and grid[xx][yy] >= grid[x][y]:
                    q1.append([xx,yy])
                    v1[xx][yy] = True
        while q2:
            x,y = q2.popleft()
            for k in range(4):
                xx = x+dx[k]
                yy = y+dy[k]
                if xx > -1 and yy > -1 and xx < n and yy < m and not v2[xx][yy] and grid[xx][yy] >= grid[x][y]:
                    q2.append([xx,yy])
                    v2[xx][yy] = True

        for i in range(n):
            for j in range(m):
                if v1[i][j] and v2[i][j]:
                    ans.append([i,j])
        # print(v1)
        return ans