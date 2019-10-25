class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    dungeon[i][j] = max(1, 1 - dungeon[i][j])
                elif j == n - 1:
                    dungeon[i][j] = max(1, dungeon[i + 1][j] - dungeon[i][j])
                elif i == m - 1:
                    dungeon[i][j] = max(1, dungeon[i][j + 1] - dungeon[i][j])
                else:
                    dungeon[i][j] = max(1, min(dungeon[i + 1][j], dungeon[i][j + 1]) - dungeon[i][j])
        return dungeon[0][0]