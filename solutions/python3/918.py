class Solution:
    def maxSubarraySumCircular(self, A):
        lMn, rMx, res, lSm, rSm, preSm = float("inf"), [-float("inf")] * (len(A) + 1), -float("inf"), 0, 0, 0
        for i in range(len(A) - 1, -1, -1):
            rSm += A[i]
            rMx[i] = max(rMx[i + 1], rSm)
        for i in range(len(A)):
            preSm += A[i]
            lMn = min(lMn, lSm)
            res = max(res, preSm, preSm - lMn, preSm + rMx[i + 1])
            lSm += A[i]
        return res