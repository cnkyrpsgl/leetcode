class Solution:
    def multiply(self, A, B):
        return [[sum(a * b for a, b in zip(A[i], [B[k][j] for k in range(len(B))])) for j in range(len(B[0]))] for i in range(len(A))]