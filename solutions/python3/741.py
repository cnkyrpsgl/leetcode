class Solution(object):
    def cherryPickup(self, grid):
        if grid[-1][-1] == -1: return 0
        memo, n = {}, len(grid)
        def dp(i1, j1, i2, j2):
            if (i1, j1, i2, j2) in memo: return memo[(i1, j1, i2, j2)]
            if n in (i1, j1, i2, j2) or -1 in (grid[i1][j1], grid[i2][j2]): return -1
            if i1 == i2 == j1 == j2 == n - 1: return grid[-1][-1]
            mx = max(dp(i1+1, j1, i2+1, j2), dp(i1+1, j1, i2, j2+1), dp(i1, j1+1, i2+1, j2), dp(i1, j1+1, i2, j2+1))
            if mx == - 1: out = -1 
            elif i1 == i2 and j1 == j2: out = mx + grid[i1][j1]
            else: out = mx + grid[i1][j1] + grid[i2][j2]
            memo[(i1, j1, i2, j2)] = out
            return out
        return max(0, dp(0, 0, 0, 0))