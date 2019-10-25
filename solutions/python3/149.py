# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points):
        m, res, roots = {}, 0, set()
        for i, p1 in enumerate(points):
            if (p1.x, p1.y) not in roots:
                roots.add((p1.x, p1.y))
                m.clear()
                dup = path = 0
                for j, p2 in enumerate(points):
                    if i != j:
                        try:
                            cur = (p1.y - p2.y) * 100 / (p1.x - p2.x)
                        except:
                            if p1.y == p2.y:
                                dup += 1
                                continue
                            else:
                                cur = "ver"
                        m[cur] = m.get(cur, 0) + 1
                        if m[cur] > path:
                            path = m[cur]
                if path + dup + 1 > res:
                    res = path + dup + 1
        return res