class Solution:
    def hasGroupsSizeX(self, deck):
        import functools
        def gcd(a, b):
            if not b: return a
            return gcd(b, a % b)
        return functools.reduce(gcd, collections.Counter(deck).values()) != 1