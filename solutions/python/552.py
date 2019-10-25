class Solution:
    def checkRecord(self, n):
        dp, mod = [1, 0, 0, 1, 1, 0], 10 ** 9 + 7
        for i in range(1, n):
            dp[0], dp[1], dp[2], dp[3], dp[4], dp[5] = sum(dp) % mod, dp[0], dp[1], sum(dp[3:]) % mod, dp[3], dp[4]
        return sum(dp) % mod