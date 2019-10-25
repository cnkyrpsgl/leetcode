class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n *= -1
            x = 1 / x
        elif not n:
            return 1
        half = self.myPow(x, n // 2)
        return x * half * half if n % 2 else half * half