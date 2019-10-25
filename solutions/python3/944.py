class Solution:
    def minDeletionSize(self, A):
        return sum(any(a[j] > b[j] for a, b in zip(A, A[1:])) for j in range(len(A[0])))