class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1:
            return -1
        bfs = [[0, 0]]
        cnt = 1
        seen = {(0, 0)}
        while bfs:
            new = []
            for i, j in bfs:
                for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1):
                    if 0 <= x < n and 0 <= y < n and (x, y) not in seen and not grid[x][y]:
                        if x == y == n - 1:
                            return cnt + 1
                        new.append((x, y))
                        seen.add((x, y))
            cnt += 1
            bfs = new
        return -1