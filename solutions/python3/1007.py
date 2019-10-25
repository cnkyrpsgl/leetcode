class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        res = min(len(A) - max(A.count(c), B.count(c)) if all(a == c or b == c for a, b in zip(A, B)) else float('inf') for c in (A[0], B[0]))
        return res if res < float('inf') else -1