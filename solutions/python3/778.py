class Solution:
    def swimInWater(self, grid):
        heap, res, n, visited = [(grid[0][0], 0, 0)], 0, len(grid), set()
        while True:
            d, i, j = heapq.heappop(heap)
            if d > res: res = d
            if i == j == n - 1: return res
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and (x, y) not in visited: 
                    visited.add((x, y))
                    heapq.heappush(heap, (grid[x][y], x, y))