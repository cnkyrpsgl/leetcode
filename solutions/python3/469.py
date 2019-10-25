class Solution:
    def isConvex(self, points):
        def direction(a, b, c): return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        d, n = 0, len(points)
        for i in range(n):
            a = direction(points[i], points[(i + 1) % n], points[(i + 2) % n])
            if not d: d = a
            elif a * d < 0: return False
        return True