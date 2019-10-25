class Solution:
    def maxProfit(self, k, prices):
        if k >= len(prices) // 2: return sum(sell - buy for sell, buy in zip(prices[1:], prices[:-1]) if sell - buy > 0)
        dp = [[0, -float("inf")] for _ in range(k + 1)]
        for p in prices:
            for i in range(k + 1):
                if i and dp[i - 1][1] + p > dp[i][0]: dp[i][0] = dp[i - 1][1] + p 
                if dp[i][0] - p > dp[i][1]: dp[i][1] = dp[i][0] - p
        return dp[-1][0]