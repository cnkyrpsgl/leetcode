class Solution:
    def minDeletionSize(self, A):
        m, n = len(A), len(A[0])
        dp = [1] * n
        for j in range(1, n):
            for i in range(j):
                if all(A[k][i] <= A[k][j] for k in range(m)):
                    dp[j] = max(dp[j], dp[i] + 1)
        return n - max(dp)