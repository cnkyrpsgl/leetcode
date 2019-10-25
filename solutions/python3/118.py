class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = numRows and [[1]] or []
        for _ in range(numRows-1):
            res.append([1] + [a + b for a, b in zip(res[-1], res[-1][1:])] + [1])
        return res