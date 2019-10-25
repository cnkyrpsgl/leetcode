class Solution:
    def largestOverlap(self, A, B):
        n, shift, rn = len(A), range(-1 * len(A) + 1, len(A)), range(len(A))
        return max(sum(A[i][j] and B[i + v][j + h] for i in rn for j in rn if 0 <= i + v < n > j + h >= 0) for h in shift for v in shift)   