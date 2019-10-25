class Solution:
    def leastOpsExpressTarget(self, x: int, y: int) -> int:
        pos = neg = k = 0
        while y:
            y, cur = divmod(y, x)
            if k:
                pos, neg = min(cur * k + pos, (cur + 1) * k + neg), min((x - cur) * k + pos, (x - cur - 1) * k + neg)
            else:
                pos, neg = cur * 2, (x - cur) * 2
            k += 1
        return min(pos, k + neg) - 1