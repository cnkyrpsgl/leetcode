class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        pre = []
        for i in range(len(A) - 1, -1, -1):
            bisect.insort_left(pre, (A[i], i))
            if pre.index((A[i], i)):
                j = pre[pre.index((A[i], i)) - 1][1]
                A[i], A[j] = A[j], A[i]
                break
        return A