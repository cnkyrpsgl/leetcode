class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def dirToIndex(x, y, d):
            if d == "r": return (x, y + 1, d) if y + 1 < n and matrix[x][y + 1] == 0 else (x + 1, y, "d")
            elif d == "d": return (x + 1, y, d) if x + 1 < n and matrix[x + 1][y] == 0 else (x, y - 1, "l")
            elif d == "l": return (x, y - 1, d) if y > 0 and matrix[x][y - 1] == 0 else (x - 1, y, "u")
            else: return (x - 1, y, d) if x > 0 and matrix[x - 1][y] == 0 else (x, y +1, "r")
        matrix = [[0 for i in range(1, n + 1)] for j in range(n)]
        num, dir, i, j = 1, "r", 0, 0
        while 0 <= i < n and 0 <= j < n and matrix[i][j] == 0:
            matrix[i][j] = num
            num += 1
            i, j, dir = dirToIndex(i, j, dir)
        return matrix        