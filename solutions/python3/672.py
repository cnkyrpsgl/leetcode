class Solution:
    def flipLights(self, n, m):
        n = min(n, 3)
        return min(1 << n, 1 + m * n)