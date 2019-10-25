class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0] == 1: return 0
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])): 
                if obstacleGrid[i][j] == 1 or i == j == 0:
                    obstacleGrid[i][j] -= 1
                else:
                    add1 = obstacleGrid[i - 1][j] if i > 0 else 0
                    add2 = obstacleGrid[i][j - 1] if j > 0 else 0
                    obstacleGrid[i][j] += add1 + add2
        return abs(obstacleGrid[-1][-1])