class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        return not all(((c - i ** 2) ** 0.5) % 1 for i in range(int(c ** 0.5) + 1))