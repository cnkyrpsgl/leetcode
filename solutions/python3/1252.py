from collections import Counter as cnt


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row, col = cnt(r for r, c in indices), cnt(c for r, c in indices)
        return sum((row[i] + col[j]) % 2 for i in range(n) for j in range(m))
