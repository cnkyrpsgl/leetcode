class Solution:
    def maxSumSubmatrix(self, matrix, k, mxTotal = -float("inf")):
        for l in range(len(matrix[0])):
            dp = [0] * len(matrix)
            for r in range(l, len(matrix[0])):
                for i in range(len(matrix)):
                    dp[i] += matrix[i][r]
                sums, cur, mx = [float("inf")], 0, -float("inf")
                for sm in dp:
                    bisect.insort(sums, cur)
                    cur += sm
                    mx = max(mx, cur - sums[bisect.bisect_left(sums, cur - k)])
                mxTotal = max(mxTotal, mx)
        return mxTotal