class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        for l in range(len(S), 0, -1):
            s = S[:l]
            seen = {s}
            for j in range(l, len(S)):
                s = s[1:] + S[j]
                if s in seen:
                    return l
                seen.add(s)
        return 0
                