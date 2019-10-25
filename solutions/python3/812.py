class Solution:
    def largestTriangleArea(self, p):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        from itertools import combinations as cb
        def f(p1, p2, p3):
            (x1, y1), (x2, y2), (x3, y3) = p1,p2,p3
            return 0.5 * abs(x2 * y3 + x1 * y2 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3)
        return max(f(a, b, c) for a, b, c in cb(p, 3))