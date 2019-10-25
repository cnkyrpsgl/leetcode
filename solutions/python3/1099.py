class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        res, l, r = -1, 0, len(A) - 1
        while l < r:
            if A[l] + A[r] >= K:
                r -= 1
            else:
                res = max(res, A[l] + A[r])
                l += 1
        return res