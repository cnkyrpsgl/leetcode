class Solution:
    def countCornerRectangles(self, grid):
        ends, res = collections.defaultdict(int), 0
        for row in grid:
            for i in range(len(row) - 1):
                for j in range(i + 1, len(row)):
                    if row[i] and row[j]:
                        ends[(i, j)] = ends.get((i, j), 0) + 1
                        res += ends[(i, j)] - 1
        return res