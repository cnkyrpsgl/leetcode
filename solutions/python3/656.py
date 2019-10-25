class Solution:
    def cheapestJump(self, A, B): 
        n = len(A)
        preMin = {n - 1:[n]}
        for i in range(n - 2, -1, -1):
            if A[i] == -1:
                continue
            mn, preIndex = float("inf"), None
            for ind in range(i + 1, i + B + 1 <= n and i + B + 1 or n):
                if -1 < A[ind] < mn:
                    mn, preIndex = A[ind], ind
            if preIndex:
                A[i] += A[preIndex]
                preMin[i] = preMin[preIndex] + [i + 1]
            else:
                A[i] = -1
        return 0 in preMin and preMin[0][::-1] or []