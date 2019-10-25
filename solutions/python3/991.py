class Solution:
    def brokenCalc(self, X, Y):
        res = 0
        while X < Y:
            res += Y % 2 + 1
            Y = (Y + 1) // 2
        return res + X - Y