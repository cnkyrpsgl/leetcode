class Solution:
    def numberOfArithmeticSlices(self, A):
        dp, res = collections.defaultdict(dict), 0
        for j in range(len(A)):
            for i in range(j):
                dp[j][A[j] - A[i]] = dp[j].get(A[j] - A[i], 0) + dp[i].get(A[j] - A[i], 1) 
                if A[j] - A[i] in dp[i]: res, dp[j][A[j] - A[i]] = res + dp[i][A[j] - A[i]], dp[j][A[j] - A[i]] + 1
        return res           