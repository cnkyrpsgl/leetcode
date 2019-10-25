class Solution:
    def fractionToDecimal(self, n, d):
        res = ["-"] if n * d < 0 else [""]
        n, d = abs(n), abs(d)
        res.append(str(n // d))
        n %= d
        if not n: return "".join(res)
        res.append(".")
        mp = {n: len(res)}
        while n:
            n *= 10
            res.append(str(n // d))
            n %= d
            if n in mp:
                res.insert(mp[n], "(")
                res.append(")")
                break
            mp[n] = len(res)
        return "".join(res)