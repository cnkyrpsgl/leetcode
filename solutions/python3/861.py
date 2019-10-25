class Solution:
    def matrixScore(self, A):
        for i, row in enumerate(A):
            if not row[0]:
                A[i] = [1 - num for num in row]
        m, n, sm = len(A), len(A and A[0]), 0
        for c in range(n):
            cnt = sum(A[r][c] for r in range(m))
            sm += max(cnt, m - cnt) * 2 ** (n - c - 1)
        return sm