class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        return len(set(a[0] == b[0] or (b[1] - a[1]) / (b[0] - a[0]) for a, b in zip(c, c[1:]))) == 1