class Solution:
    def findDiagonalOrder(self, matrix):
        i, j, d, res, n, m = 0, 0, 1, [], len(matrix), len(matrix and matrix[0]) 
        while i < n and j < m:
            res.append(matrix[i][j])
            if j + 1 < m and (i == 0 and d == 1) or (i == n - 1 and d == -1): j, d = j + 1, -d
            elif i + 1 < n and (j == 0 and d == -1) or (j == m - 1 and d == 1): i, d = i + 1, -d
            elif d == 1: i, j = i - 1, j + 1
            else: i, j = i + 1, j - 1
        return res