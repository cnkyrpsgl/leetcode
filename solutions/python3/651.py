class Solution:
    def maxA(self, N):
        dp = [0] * (N + 1)
        for i in range(N + 1):
            dp[i] = i
            for j in range(1, i - 2):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        return dp[N]