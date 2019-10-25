
class Solution:
    def minAreaFreeRect(self, points):
        mn, st, n = float('inf'), {(x, y) for x, y in points}, len(points) 
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    if not (x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1) and (x3 + (x2 - x1), y3 + (y2 - y1)) in st:
                        mn = min(mn, ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 * ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5)
        return mn if mn < float("inf") else 0