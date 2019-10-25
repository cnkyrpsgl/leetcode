class Solution:
    def minTotalDistance(self, grid):
        m, n = len(grid), len(grid[0])
        x, y = sorted(i for i in range(m) for j in range(n) if grid[i][j]), sorted(j for i in range(m) for j in range(n) if grid[i][j])
        avg_x = len(x) % 2 and x[len(x) // 2] or (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2
        avg_y = len(y) % 2 and y[len(y) // 2] or (y[len(y) // 2 - 1] + y[len(y) // 2]) / 2
        return int(sum(abs(avg_x - i) + abs(avg_y - j) for i, j in zip(x, y)))