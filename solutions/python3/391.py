class Solution:
    def isRectangleCover(self, rectangles):
        cnt = collections.Counter()
        for x1, y1, x2, y2 in rectangles:
            cnt[(x1, y1)] += 1
            cnt[(x1, y2)] += 1
            cnt[(x2, y2)] += 1
            cnt[(x2, y1)] += 1
        x1, y1, x2, y2 = min([r[:2] for r in rectangles]) + max(r[-2:] for r in rectangles)
        for x, y in ((x1, y1), (x1, y2), (x2, y2), (x2, y1)):
            if cnt[(x, y)] != 1: return False
            cnt.pop((x, y))
        return all(cnt[k] in (2, 4) for k in cnt) and sum((x2 - x1) * (y2 - y1) for x1, y1, x2, y2 in rectangles) == (x2 - x1) * (y2 - y1)