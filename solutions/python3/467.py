class Solution:
    def findSubstringInWraproundString(self, p):
        res, l = {i: 1 for i in p}, 1
        for i, j in zip(p, p[1:]):
            l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            res[j] = max(res[j], l)
        return sum(res.values())