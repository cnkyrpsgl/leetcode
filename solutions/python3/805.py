class Solution:
    def splitArraySameAverage(self, A):
        def find(target, k, i):
            if (target,k) in not_found and not_found[(target,k)] <= i: return False
            if k == 0: return target == 0
            if k + i > len(A): return False
            res = find(target - A[i], k - 1, i + 1) or find(target, k, i + 1)
            if not res: not_found[(target, k)] = min(not_found.get((target, k), n), i)
            return res
        not_found = dict()
        n, s = len(A), sum(A)
        return any(find(s * i / n, i, 0) for i in range(1, n // 2 + 1) if s * i % n == 0)