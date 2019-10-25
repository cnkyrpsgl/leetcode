class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        m, n = len(a), len(b)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] else max(dp[i][j - 1], dp[i - 1][j])
        return dp[-1][-1]