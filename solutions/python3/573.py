class Solution:
    def minDistance(self, height, width, t, s, n):
        sm = 2 * sum(abs(x - t[0]) + abs(y - t[1]) for x, y in n)
        return min(sm - abs(x - t[0]) - abs(y - t[1]) + abs(x - s[0]) + abs(y - s[1]) for x, y in n)