class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        q, move, n, seen = {(0, 1, 0)}, 0, len(grid), set()
        while q:
            new = set()
            for i, j, hv in q:
                if i == j == n - 1 and not hv:
                    return move
                if hv and i < n - 1 and not grid[i + 1][j]:
                    if (i + 1, j, 1) not in seen:
                        new.add((i + 1, j, 1))
                if hv and j + 1 < n and grid[i][j + 1] == grid[i - 1][j + 1] == 0:
                    if (i, j + 1, 1) not in seen:
                        new.add((i, j + 1, 1))
                    if (i - 1, j + 1, 0) not in seen:
                        new.add((i - 1, j + 1, 0))
                if not hv and j + 1 < n and not grid[i][j + 1]:
                    if (i, j + 1, 0) not in seen:
                        new.add((i, j + 1, 0))
                if not hv and i + 1 < n and grid[i + 1][j] == grid[i + 1][j - 1] == 0:
                    if (i + 1, j, 0) not in seen:
                        new.add((i + 1, j, 0))
                    if (i + 1, j - 1, 1) not in seen:
                        new.add((i + 1, j - 1, 1))
            q = new
            seen |= new
            move += 1
        return -1