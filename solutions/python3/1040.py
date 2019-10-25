class Solution:
    def numMovesStonesII(self, A: List[int]) -> List[int]:
        A.sort()
        i, n, low = 0, len(A), len(A)
        high = max(A[-1] - n + 2 - A[1], A[-2] - A[0] - n + 2)
        for j in range(n):
            while A[j] - A[i] >= n: i += 1
            if j - i + 1 == n - 1 and A[j] - A[i] == n - 2:
                low = min(low, 2)
            else:
                low = min(low, n - (j - i + 1))
        return [low, high]