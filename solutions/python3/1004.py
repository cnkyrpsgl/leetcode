class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeros, res = [-1] + [i for i, c in enumerate(A) if not c] + [len(A)], 0
        for j in range(K + 1, len(zeros)):
            res = max(res, zeros[j] - zeros[j - K - 1] - 1)
        return res or K and len(A)