class Solution:
    def minFlipsMonoIncr(self, s):
        res = cur = s.count("0")
        for c in s: res, cur = c == "1" and (res, cur + 1) or (min(res, cur - 1), cur - 1)
        return res