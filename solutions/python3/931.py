class Solution:
    def minFallingPathSum(self, A):
        for i in range(1, len(A)):
            for j in range(len(A)):
                A[i][j] += min(A[i - 1][j and j - 1:j + 2])
        return min(A[-1])