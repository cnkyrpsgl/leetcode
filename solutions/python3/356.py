class Solution:
    def isReflected(self, points):
        if len(points) < 2:
            return True
        x = (min(x for x, y in points) + max(x for x, y in points)) / 2 
        left, right, on = set(), set(), set()
        for i, j in points:
            if i < x:
                left.add((i, j))
            elif i > x:
                right.add((i, j))
            else:
                on.add((i, j))
        for i, j in points:
            if i < x and (2 * x - i, j) in right:
                continue
            elif i > x and (2 * x - i, j) in left:
                continue
            elif i == x and (2 * x - i, j) in on:
                continue
            else:
                return False
        return True