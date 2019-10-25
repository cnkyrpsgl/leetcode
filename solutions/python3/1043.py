class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0] * (N + K)
        for i in range(N):
            curMax = 0
            for k in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i - k + 1])
                dp[i] = max(dp[i], dp[i - k] + curMax * k)
        return dp[N - 1]