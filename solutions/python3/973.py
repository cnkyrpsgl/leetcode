class Solution:
    def kClosest(self, points, K):
        return sorted(points, key = lambda p: p[0] ** 2 + p[1] ** 2)[:K]