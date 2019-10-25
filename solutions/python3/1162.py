class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = [[i, j] for i in range(n) for j in range(n) if grid[i][j]]
        d = -1
        while q and len(q) != n ** 2:
            Q = []
            for i, j in q:
                for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if 0 <= x < n > y >= 0 and not grid[x][y]:
                        grid[x][y] = 1
                        Q.append([x, y])
            q = Q
            d += 1
        return d
            
            