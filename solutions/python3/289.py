class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        matrix = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                cnt = 0
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i + 1, j + 1), (i - 1, j + 1), (i + 1, j - 1)):
                    if 0 <= x < m and 0 <= y < n and board[x][y] == 1: cnt += 1
                if (board[i][j] and 2 <= cnt <= 3) or (not board[i][j] and cnt == 3): matrix[i][j] = 1
        for i in range(m):
            for j in range(n):
                board[i][j] = matrix[i][j]