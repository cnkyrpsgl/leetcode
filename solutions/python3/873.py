class Solution:
    def lenLongestFibSubseq(self, A):
        n, pair, res, back = len(A), {}, 0, set()
        for i in range(n):
            back.add(A[i])
            j = i + 1
            mx = 2 * A[i]
            while j < n and A[j] < mx:
                if (A[j] - A[i], A[i]) in pair:
                    pair[(A[i], A[j])] = pair[(A[j] - A[i], A[i])] + 1
                else:
                    pair[(A[i], A[j])] = A[j] - A[i] in back and 3 or 2
                res = max(res, pair[(A[i], A[j])])
                j += 1
        return res > 2 and res or 0