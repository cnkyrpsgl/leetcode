class Solution:
    def numTilings(self, N):
        dp = [[0, 0] for _ in range(N + 1)]
        dp[0][0] = 1
        for i in range(N):
            if i + 1 <= N:
                dp[i + 1][0] += dp[i][0] + dp[i][1]
                dp[i + 1][1] += dp[i][1]
            if i + 2 <= N:
                dp[i + 2][0] += dp[i][0]
                dp[i + 2][1] += 2 * dp[i][0]
        return dp[-1][0] % (10 ** 9 + 7)