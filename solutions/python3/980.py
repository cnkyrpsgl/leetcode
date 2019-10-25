class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def dfs(i, j, visited):
            if grid[i][j] == 2:
                self.walks += visited == self.visit
                return
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and grid[x][y] != -1:
                    grid[i][j] -= 1
                    dfs(x, y, visited + 1)
                    grid[i][j] += 1
        m, n = len(grid), len(grid[0])
        self.visit = m * n - sum(c == -1 for row in grid for c in row)
        self.walks = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    grid[i][j] -= 1
                    dfs(i, j, 1)
        return self.walks