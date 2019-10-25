class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j, ret=True):
            grid[i][j] = -1
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n:
                    if not grid[x][y]:
                        ret &= dfs(x, y)
                else:
                    ret = False
            return ret

        m, n = len(grid), len(grid[0])
        return sum(dfs(i, j) for i in range(m) for j in range(n) if grid[i][j] == 0)

