class Solution:
    def palindromePairs(self, words):
        index, res = {w:i for i, w in enumerate(words)}, []
        for i, w in enumerate(words):
            for j in range(len(w) + 1):
                pre, suf = w[:j], w[j:]
                if pre == pre[::-1]:
                    suf = suf[::-1]
                    if suf != w and suf in index:
                        res.append([index[suf], i])
                if j != len(w) and suf == suf[::-1]:
                    pre = pre[::-1]
                    if pre != w and pre in index:
                        res.append([i, index[pre]])
        return res