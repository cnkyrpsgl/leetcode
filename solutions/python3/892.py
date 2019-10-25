class Solution:
    def surfaceArea(self, grid):
        n, sm = len(grid), 0
        for i in range(n):
            for j in range(n):
                sm += grid[i][j] and grid[i][j] * 4 + 2
                if i > 0: sm -= min(grid[i - 1][j], grid[i][j])
                if j > 0: sm -= min(grid[i][j - 1], grid[i][j])
                if i < n - 1: sm -= min(grid[i + 1][j], grid[i][j])
                if j < n - 1: sm -= min(grid[i][j + 1], grid[i][j])
        return sm