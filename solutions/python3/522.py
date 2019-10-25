class Solution:
    def findLUSlength(self, strs):
        def find(s, t):
            i = 0
            for c in t:
                if c == s[i]: i += 1
                if i == len(s): return True
            return False
        for s in sorted(strs, key=len, reverse=True):
            if sum(find(s, t) for t in strs) == 1: return len(s)
        return -1