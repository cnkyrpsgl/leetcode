class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.res = 0
        used = set()
        def dfs(i, j):
            used.add((i, j))
            self.res += 4
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    self.res -= 1
                    if (x, y) not in used:
                        dfs(x, y)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in used:
                    dfs(i, j)
        return self.res