class Solution:
    def transpose(self, A):
        return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]