class Solution:
    def isRationalEqual(self, S, T):
        def f(s):
            i = s.find('(')
            if i >= 0:
                s = s[:i] + s[i + 1:-1] * 20
            return float(s[:20])
        return f(S) == f(T)