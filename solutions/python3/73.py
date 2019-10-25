class Solution:
    def setZeroes(self, matrix):
        m, n, x = len(matrix), len(matrix and matrix[0]), 0
        for i in range(m):
            for j in range(n):
                if i < m - 1 and not matrix[i][j] and matrix[i + 1][j]: matrix[i + 1][j] = None
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i > 0 and not matrix[i][j] and matrix[i - 1][j]: matrix[i - 1][j] = None
        while x < m:
            y = 0
            while y < n:
                if matrix[x][y] == 0: matrix[x], y = [0] * n, n 
                elif not matrix[x][y]: matrix[x][y] = 0
                y += 1 
            x += 1 