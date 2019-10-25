class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return max(0.5, 1 / n)