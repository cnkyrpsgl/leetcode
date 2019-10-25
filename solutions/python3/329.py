class Solution:
    def longestIncreasingPath(self, matrix):
        def dfs(i, j):
            if not dp[i][j]:
                dp[i][j] = 1+max((dfs(x,y) for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)) if 0 <=x<m and 0<=y<n and matrix[x][y] > matrix[i][j]),default=0)
            return dp[i][j]
        m, n, = len(matrix), len(matrix and matrix[0])
        dp = [[0] * n for _ in range(m)]
        return max((dfs(i,j) for i in range(m) for j in range(n)),default=0)