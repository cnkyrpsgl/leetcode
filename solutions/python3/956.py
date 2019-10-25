class Solution:
    def tallestBillboard(self, rods):
        dp = {0: 0}
        for x in rods:
            for d, h in list(dp.items()):
                dp[d + x] = max(dp.get(x + d, 0), h)
                dp[abs(d - x)] = max(dp.get(abs(d - x), 0), h + min(d, x))
        return dp[0]         