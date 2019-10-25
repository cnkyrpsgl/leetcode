class Solution:
    def findLongestChain(self, pairs):
        pairs.sort(key = lambda x: x[1])
        res, pre = 1, pairs[0][1]
        for c, d in pairs[1:]:
            if pre < c:
                pre = d
                res += 1
        return res