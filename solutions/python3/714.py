class Solution:
    def maxProfit(self, prices, fee):
        pre = [0, -float("inf")]
        for p in prices:
            p0, p1 = pre[1] + p - fee, pre[0] - p
            if p0 > pre[0]: pre[0] = p0
            if p1 > pre[1]: pre[1] = p1
        return pre[0]