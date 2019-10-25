class Solution:
    def minAreaRect(self, points):
        seen, bases, baseX, res = collections.defaultdict(dict), [], -1, float("inf")
        for x, y in sorted(points):
            if x != baseX:
                baseX, bases = x, []
            for base in bases:
                if y in seen[base]:
                    res = min(res, (x - seen[base][y]) * (y - base))
                seen[base][y] = x
            bases.append(y)
        return res if res < float("inf") else 0