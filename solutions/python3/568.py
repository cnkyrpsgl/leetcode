class Solution:
    def maxVacationDays(self, flights: List[List[int]], days: List[List[int]]) -> int:
        if not flights or not days:
            return 0
        n, k = len(flights), len(days[0])
        dp = [[-1] * (k + 1) for c in range(n)]
        dp[0][0] = 0
        for w in range(1, k + 1):
            for c in range(n):
                dp[c][w] = max([dp[pre][w - 1] + days[c][w - 1] for pre in range(n) if (flights[pre][c] or pre == c) and dp[pre][w - 1] >= 0] or [-1])
        return max(dp[c][-1] for c in range(n))