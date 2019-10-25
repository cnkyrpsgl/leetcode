class Solution:
    def removeInvalidParentheses(self, s):
        l = r = 0
        for c in s:
            if c.isalpha(): continue
            if c == "(": l += 1 
            elif l: l -= 1
            else: r += 1
        q = {("", l, r, 0, 0)}
        for c in s:
            new = set()
            for st, l, r, lCur, rCur in q:
                if c == "(":
                    new.add((st + c, l, r, lCur + 1, rCur))
                    if l:
                        new.add((st, l - 1, r, lCur, rCur))
                elif c == ")":
                    if lCur:
                        new.add((st + c, l, r, lCur - 1, rCur))
                    else:
                        new.add((st + c, l, r, lCur, rCur + 1))
                    if r:
                        new.add((st, l, r - 1, lCur, rCur))
                else:
                    new.add((st + c, l, r, lCur, rCur))
            q = new
        return list({st for st, l, r, lCur, rCur in q if l == r == lCur == rCur == 0})