class Solution:
    def findContentChildren(self, g, s):
        g.sort(reverse = True); s.sort(reverse = True); res = 0
        while s and g:
            if g[-1] <= s[-1]: res += 1; g.pop(); s.pop()
            else: s.pop()
        return res