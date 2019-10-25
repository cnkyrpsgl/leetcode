class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n, d = len(grid), len(grid[0]), 1
        piled = collections.defaultdict(set)
        dist = collections.defaultdict(int)
        bfs = [(i, j, i, j) for i in range(m) for j in range(n) if grid[i][j] == 1]
        total, res = len(bfs), []
        while bfs:
            new = []
            for x, y, i, j in bfs:
                for ii, jj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= ii < m and 0 <= jj < n and not grid[ii][jj] and (x, y) not in piled[(ii, jj)]:
                        piled[(ii, jj)].add((x, y))
                        dist[(ii, jj)] += d
                        if len(piled[(ii, jj)]) == total:
                            res.append(dist[(ii, jj)])
                        new.append((x, y, ii, jj))
            bfs = new
            d += 1
        return min(res) if res else -1