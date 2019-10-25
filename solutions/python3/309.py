class Solution:
    def maxProfit(self, prices):
        dp1, dp2, dp3 = 0, 0, -float("inf")
        for p in prices:
            dp1, dp2, dp3 = dp3 + p, max(dp1, dp2), max(dp2 - p, dp3)
        return max(dp1, dp2)