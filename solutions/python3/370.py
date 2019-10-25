class Solution:
    def getModifiedArray(self, length, updates):
        start, end, res, cur = collections.defaultdict(int), collections.defaultdict(int), [0] * length, 0
        for s, e, inc in updates:
            start[s] += inc
            end[e] += -inc
        for i in range(length):
            if start[i]:
                cur += start[i]
            res[i] += cur
            if end[i]:
                cur += end[i]
        return res