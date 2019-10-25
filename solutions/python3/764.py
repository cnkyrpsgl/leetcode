class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        #up, left, down, right
        dp, res, mines = [[[0, 0, 0, 0] for j in range(N)] for i in range(N)], 0, {(i, j) for i, j in mines}
        for i in range(N):
            for j in range(N):
                if (i, j) not in mines:
                    try:
                        dp[i][j][0] = dp[i - 1][j][0] + 1
                    except:
                        dp[i][j][0] = 1
                    try:
                        dp[i][j][1] = dp[i][j - 1][1] + 1
                    except:
                        dp[i][j][1] = 1
        for i in range(N - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if (i, j) not in mines:
                    try:
                        dp[i][j][2] = dp[i + 1][j][2] + 1
                    except:
                        dp[i][j][2] = 1
                    try:
                        dp[i][j][3] = dp[i][j + 1][3] + 1
                    except:
                        dp[i][j][3] = 1
                    res = max(res, min(dp[i][j]))
        return res