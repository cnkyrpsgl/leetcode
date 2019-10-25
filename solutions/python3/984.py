class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if not A and not B: return ''
        if A >= B:
            a = 2 if A >= 2 else 1
            b = 2 if A - a - B < 1 and B >= 2 else 1 if B else 0
            return a * 'a' + b * 'b' + self.strWithout3a3b(A - a, B - b)
        else:
            b = 2 if B >= 2 else 1
            a = 2 if B - b - A < 1 and A >= 2 else 1 if A else 0
            return b * 'b' + a * 'a' + self.strWithout3a3b(A - a, B - b)
            