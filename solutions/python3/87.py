class Solution:
    def isScramble(self, s1, s2):
        n, m = len(s1), len(s2)
        if n != m or sorted(s1) != sorted(s2):
            return False
        if n < 4 or s1 == s2:
            return True
        f = self.isScramble
        for i in range(1, n):
            if f(s1[:i], s2[:i]) and f(s1[i:], s2[i:]) or \u005C
               f(s1[:i], s2[-i:]) and f(s1[i:], s2[:-i]):
                return True
        return False