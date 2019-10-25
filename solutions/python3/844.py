class Solution:
    def backspaceCompare(self, S, T):
        def construct(s):
            new_s = []
            for c in s:
                if c == "#" and len(new_s) > 0:
                    new_s.pop()
                elif c != "#":
                    new_s.append(c)
            return new_s
        s, t = construct(S), construct(T)
        return s == t