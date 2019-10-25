class Solution:
    def knightDialer(self, N):
        x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
        for _ in range(N - 1):
            x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = \u005C
                x6 + x8, x7 + x9, x4 + x8, \u005C
                x7 + x9 + x0, 0, x1 + x7 + x0, \u005C
                x2 + x6, x1 + x7, x2 + x4, \u005C
                x4 + x6
        return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % (10 ** 9 + 7)