class Solution:
    def computeArea(self, a, b, c, d, e, f, g, h):
        x1, x2, x3 = abs(a - c), abs(e - g), max(a, c, e, g) - min(a, c, e, g) 
        y1, y2, y3 = abs(b - d), abs(f - h), max(b, d, f, h) - min(b, d, f, h)
        if x3 < x1 + x2 and y3 < y1 + y2: intrs = (x1 + x2 - x3) * (y1 + y2 - y3) 
        else: intrs = 0
        return x1 * y1 + x2 * y2 - intrs