class Solution:
    def crackSafe(self, n, k):
        s = '0' * (n - 1)
        D = '9876543210'[-k:]
        for _ in range(k**n):
            s += next(d for d in D if (s + d)[-n:] not in s)
        return s