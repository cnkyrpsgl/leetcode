class Solution(object):
    def findDerangement(self, n, dp = 1, mod = 10 ** 9 + 7):
        for i in range(1, n + 1): dp = (i * dp + (-1) ** i) % mod
        return dp 