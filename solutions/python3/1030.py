class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        bfs, res, seen = [[r0, c0]], [], {(r0, c0)}
        while bfs:
            res += bfs
            new = []
            for i, j in bfs:
                for x, y in (i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1):
                    if 0 <= x < R and 0 <= y < C and (x, y) not in seen:
                        seen.add((x, y))
                        new.append([x, y])
            bfs = new
        return res
                        