class Solution:
    def maxAreaOfIsland(self, grid):
        m, n = len(grid), len(grid and grid[0])
        def explore(i, j):
            grid[i][j] = 0
            return 1 + sum(explore(x,y) for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)) if 0<=x<m and 0<=y<n and grid[x][y])
        return max(grid[i][j] and explore(i, j) or 0 for i in range(m) for j in range(n))