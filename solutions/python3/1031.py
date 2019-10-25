class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        l = [0] * n
        r = [0] * n
        sm = 0 
        for i in range(M - 1):
            sm += A[i]
        for j in range(n - M + 1):
            sm += A[j + M - 1]
            for i in range(j + 1):
                r[i] = max(r[i], sm)
            sm -= A[j]
        
        sm = 0
        for i in range(n - 1, n - M, -1):
            sm += A[i]
        for i in range(n - 1, M - 2, -1):
            sm += A[i - M + 1]
            for j in range(i + 1, n):
                l[j] = max(l[j], sm)
            sm -= A[i]
            
        
        
        
        sm = 0
        for i in range(L - 1):
            sm += A[i]
        res = 0
        for j in range(n - L + 1):
            sm += A[j + L - 1]
            if j >= M:
                res = max(res, sm + l[j - 1])
            if j + L < n:
                res = max(res, sm + r[j + L])
            sm -= A[j]
        return res