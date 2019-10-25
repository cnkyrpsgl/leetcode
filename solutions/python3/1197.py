from functools import lru_cache
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i == j == 0:
                return 0
            if i == 1 and j == 0 or j == 1 and i == 0:
                return float('inf')
            return min(dfs(abs(i - 2), abs(j - 1)), dfs(abs(i - 1), abs(j - 2))) + 1
        return dfs(abs(x), abs(y))