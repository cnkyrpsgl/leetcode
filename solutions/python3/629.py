class Solution:
    def kInversePairs(self, n, k):
        dp = [1] + [0] * k
        for i in range(2, n + 1):
            for j in range(1, k + 1): dp[j] += dp[j - 1]
            for j in range(k, 0, -1): dp[j] -= j - i >= 0 and dp[j - i]
        return dp[-1] % (10 ** 9 + 7)