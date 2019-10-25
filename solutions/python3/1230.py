class Solution:
    def probabilityOfHeads(self, p: List[float], t: int) -> float:
        n = len(p)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(i + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j] * (1 - p[i - 1])
                else : 
                    dp[i][j] = (dp[i - 1][j] * (1.0 - p[i - 1])) + (dp[i - 1][j - 1] * p[i - 1])
        return dp[-1][t]
        