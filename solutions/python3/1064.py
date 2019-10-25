class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        return ([i for i in range(len(A)) if A[i] == i] + [-1])[0]