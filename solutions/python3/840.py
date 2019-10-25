class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                if sum(grid[i][j: j + 3]) == sum(grid[i + 1][j : j +3]) == sum(grid[i + 2][j:j + 3]) == sum(grid[k][j] for k in range(i, i + 3)) == sum(grid[k][j + 1] for k in range(i, i + 3)) == sum(grid[k][j + 2] for k in range(i, i + 3)) == (grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2]) == (grid[i+2][j]+ grid[i + 1][j + 1] + grid[i][j + 2]): 
                    if set(grid[i][j: j + 3] + grid[i + 1][j: j +3] + grid[i + 2][j:j + 3]) == {1,2,3,4,5,6,7,8,9}: res += 1
        return res
                