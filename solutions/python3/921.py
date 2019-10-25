class Solution:
    def minAddToMakeValid(self, S):
        r, l = 0, []
        for s in S:
            if s == "(":
                l.append(s)
            elif l:
                l.pop()
            else:
                r += 1 
        return r + len(l)