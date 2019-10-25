class Solution:
    def isToeplitzMatrix(self, matrix):
        return all(matrix[i][j] == matrix[i - 1][j - 1] for i in range(1, len(matrix)) for j in range(1, len(matrix[0])))