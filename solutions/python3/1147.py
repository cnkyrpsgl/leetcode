class Solution:
    def longestDecomposition(self, S: str) -> int:
        res, l, r = 0, "", ""
        for i, j in zip(S, S[::-1]):
            l, r = l + i, j + r
            if l == r:
                res, l, r = res + 1, "", ""
        return res