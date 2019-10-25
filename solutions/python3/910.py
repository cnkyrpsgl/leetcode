class Solution:
    def smallestRangeII(self, A, K):
        A.sort()
        return min([max(A[-1] - K, A[i] + K) - min(A[0] + K, A[i + 1] - K) for i in range(len(A) - 1)] + [A[-1] - A[0]])