class Solution:
    def stoneGameII(self, A: List[int]) -> int:
        N = len(A)
        for i in range(N - 2, -1, -1):
            A[i] += A[i + 1]
        from functools import lru_cache
        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= N: return A[i]
            return A[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))
        return dp(0, 1)