class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        dp = [0] * 3
        for a, b, c in costs:
            c1 = min(dp[1], dp[2]) + a
            c2 = min(dp[0], dp[2]) + b
            c3 = min(dp[0], dp[1]) + c
            dp = [c1, c2, c3]
        return min(dp)