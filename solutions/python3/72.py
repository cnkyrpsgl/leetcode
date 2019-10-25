class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp = [[0] * (len(w2) + 1) for i in range(len(w1) + 1)]
        for i in range(len(w1) + 1):
            for j in range(len(w2) + 1):
                if not (i and j):
                    dp[i][j] = i or j
                elif w1[i - 1] == w2[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
                else:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]