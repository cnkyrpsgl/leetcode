class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bfs, t, m, n = [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val == 2], 0, len(grid), len(grid[0])
        while bfs:
            new = []
            for i, j in bfs:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        new.append((x, y))
            bfs = new
            t += bool(bfs)
        return t if all(val != 1 for row in grid for val in row) else -1