class Solution:
    def sumSubseqWidths(self, A):
        A.sort()
        res=0
        for i in range(len(A)):
            res*=2
            res-=A[i]
            res+=A[~i]
        return res % (10**9+7)