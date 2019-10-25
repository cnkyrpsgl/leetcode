class Solution(object):
    def guessNumber(self, n):
        l, r, g = 1, n, 1
        while g and l <= r:
            m = (l + r) // 2
            g = guess(m)
            if g == 1:
                l = m + 1
            else:
                r = m
        return m