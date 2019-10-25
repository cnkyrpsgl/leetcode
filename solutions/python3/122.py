class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # stock, no stock
        dp = [-float('inf'), 0]
        for p in prices:
            x = max(dp[1] - p, dp[0])
            y = max(dp[1], dp[0] + p)
            dp = [x, y]
        return dp[-1]