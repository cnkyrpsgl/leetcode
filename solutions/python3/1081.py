class Solution:
    def smallestSubsequence(self, S: str) -> str:
        last = {c: i for i, c in enumerate(S)}
        res = ""
        left = 0
        while last:
            right = min(last.values())
            c, i = min((S[i], i) for i in range(left, right + 1) if S[i] not in res)
            left = i + 1
            res += c
            del last[c]
        return res