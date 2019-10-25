class Solution:
    def maximalRectangle(self, matrix):
        res, m, n = 0, len(matrix), len(matrix and matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != "0":
                    if j > 0 and matrix[i][j - 1] != "0":
                        matrix[i][j] = matrix[i][j - 1] + 1
                    else:
                        matrix[i][j] = 1
                    mn, sm, k = matrix[i][j], 0, i + 1
                    while k > 0 and matrix[k - 1][j] != "0":
                        if matrix[k - 1][j] < mn:
                            sm, mn = (i - k + 2) * matrix[k - 1][j], matrix[k - 1][j]
                        else:
                            sm += mn
                        if sm > res:
                            res = sm
                        k -= 1
        return res