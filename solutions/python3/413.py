class Solution:
    def numberOfArithmeticSlices(self, A):
        if len(A) < 3:
            return 0
        A.append(float("inf"))
        d, l, n, res = A[1] - A[0], 0, len(A), 0
        for i in range(2, n):
            if d != A[i] - A[i - 1]:
                diff = i - l - 2
                if diff > 0:
                    res += diff * (diff + 1) // 2
                d, l = A[i] - A[i - 1], i - 1
        return res