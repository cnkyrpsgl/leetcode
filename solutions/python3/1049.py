class Solution:
    def lastStoneWeightII(self, A: List[int]) -> int:
        dp = {0}
        sumA = sum(A)
        for a in A:
            dp |= {a + i for i in dp}
        return min(abs(sumA - i - i) for i in dp)