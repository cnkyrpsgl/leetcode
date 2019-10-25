class Solution:
    def findMinArrowShots(self, p):
        p.sort(key = lambda x: x[1])
        (res, curr) = (1, p[0][1]) if p else (0, None)
        for n in p:
            if n[0] > curr: res, curr = res + 1, n[1]
        return res