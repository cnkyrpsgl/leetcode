class Solution:
    def largestSumOfAverages(self, A, K):
        memo = {}
        def search(n, k):
            if n < k: return 0
            if (n, k) not in memo:
                if k == 1: memo[n, k] = sum(A[:n]) / float(n)
                else:
                    cur = memo[n, k] = 0
                    for i in range(n - 1, 0, -1):
                        cur += A[i]
                        memo[n, k] = max(memo[n, k], search(i, k - 1) + cur / float(n - i))
            return memo[n, k]
        return search(len(A), K)