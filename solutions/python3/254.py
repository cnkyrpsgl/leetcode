class Solution:
    def getFactors(self, n):
        factors = set()
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors |= {i, n // i}
        q, res = [[f, [f]] for f in factors], []
        while q:
            new = []
            for sm, arr in q:
                for f in factors:
                    if f >= arr[-1]:
                        if sm * f < n:
                            new.append([sm * f, arr + [f]])
                        elif sm * f == n:
                            res.append(arr + [f])
            q = new
        return res