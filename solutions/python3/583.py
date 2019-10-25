class Solution:
    def minDistance(self, w1, w2):
        m, n = len(w1), len(w2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif w1[i - 1] == w2[j - 1]: 
                    dp[i][j] = dp[i - 1][j - 1]
                else: 
                    dp[i][j] = min(dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        return dp[-1][-1]