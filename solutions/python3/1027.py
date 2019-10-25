class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a, b = A[i], A[j]
                dp[b - a, j] = max(dp[b - a, j], dp[b - a, i] + 1)
        return max(dp.values()) + 1