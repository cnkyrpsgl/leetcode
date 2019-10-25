class Solution:
    def findLonelyPixel(self, grid: List[List[str]]) -> int:
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B':
                    rows[i].append(j)
                    cols[j].append(i)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'B' and rows[i] == [j] and cols[j] == [i]:
                    res += 1
        return res