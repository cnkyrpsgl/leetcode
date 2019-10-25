class Solution:
    def maxKilledEnemies(self, grid):
        m, n, res = len(grid), len(grid and grid[0]), 0
        dp = [[[0, 0, 0, 0] for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    dp[i][j][0] = dp[i][j - 1][0]
                    dp[i][j][1] = dp[i - 1][j][1]
                elif grid[i][j] == "E":
                    dp[i][j][0] = dp[i][j - 1][0] + 1
                    dp[i][j][1] = dp[i - 1][j][1] + 1 
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == "0":
                    dp[i][j][2] = dp[i][j + 1][2]
                    dp[i][j][3] = dp[i + 1][j][3]
                elif grid[i][j] == "E":
                    dp[i][j][2] = dp[i][j + 1][2] + 1
                    dp[i][j][3] = dp[i + 1][j][3] + 1
                if grid[i][j] == "0":
                    res = max(res, sum(dp[i][j]))
        return res        