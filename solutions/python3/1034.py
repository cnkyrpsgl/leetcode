class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        def dfs(i, j):
            seen.add((i, j))
            if not (0 < i < m - 1 and 0 < j < n - 1 and grid[i - 1][j] == grid[i + 1][j] == grid[i][j - 1] == grid[i][j + 1] == grid[i][j]):
                matrix[i][j] = 0
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] == self.tar and (x, y) not in seen:
                    dfs(x, y)
        m, n = len(grid), len(grid[0])
        seen = set()
        self.tar = grid[r0][c0]
        matrix = [row[:] for row in grid]
        dfs(r0, c0)
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[i][j] = color
        return matrix