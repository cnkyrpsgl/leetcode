class Solution:
    def numWays(self, n, k):
        same, dif = 0, k
        for _ in range(1, n): same, dif = dif, (same + dif) * (k - 1)
        return n and same + dif or 0