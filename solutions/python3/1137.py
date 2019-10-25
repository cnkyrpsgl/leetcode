class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        for _ in range(n):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        return t0
        