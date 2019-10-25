class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        res = 0
        for row in matrix:
            inv = [1 - r for r in row]
            res = max(res, sum(row == r or inv == r for r in matrix))
        return res
            