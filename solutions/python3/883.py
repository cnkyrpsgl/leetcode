class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        top = sum(grid[i][j] != 0 for i in range(n) for j in range(n))
        front = sum(max(grid[i]) for i in range(n))
        side = sum(max(grid[i][j] for i in range(n)) for j in range(n))
        return top + front + side