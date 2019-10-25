class Solution:
    def findLongestWord(self, s, d):
        d.sort(key = lambda x: (-len(x), x))
        for w in d:
            i = 0
            for c in s:
                if c == w[i]: i += 1
                if i == len(w): return w
        return ""