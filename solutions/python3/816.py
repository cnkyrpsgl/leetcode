class Solution:
    def ambiguousCoordinates(self, S):
        def properInt(s):
            return len(s) > 1 and s[0] != "0" or len(s) == 1
        
        def properFloat(s, i):
            return s[-1] not in ".0" and properInt(s[:i])
        
        s, res = S[1:-1], set()
        for i in range(len(s)):
            n1, n2 = s[:i + 1], s[i + 1:]
            p1, p2 = properInt(n1), properInt(n2)
            if p1 and p2:
                res.add("({}, {})".format(n1, n2))
            for j in range(len(n1)):
                for k in range(len(n2)):
                    n1f = n1[:j + 1] + "." + n1[j + 1:]
                    n2f = n2[:k + 1] + "." + n2[k + 1:]
                    p1f = properFloat(n1f, j + 1)
                    p2f = properFloat(n2f, k + 1)
                    if p1f and p2f:
                        res.add("({}, {})".format(n1f, n2f))
                    if p1f and p2:
                        res.add("({}, {})".format(n1f, n2))
                    if p1 and p2f:
                        res.add("({}, {})".format(n1, n2f))
        return list(res)