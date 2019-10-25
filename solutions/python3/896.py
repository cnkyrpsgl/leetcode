class Solution:
    def isMonotonic(self, A):
        return all(A[i] <= A[i - 1] for i in range(1, len(A))) or all(A[i] >= A[i - 1] for i in range(1, len(A)))