class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board and board[0])

        def explore(i, j):
            board[i][j] = "S"
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                    explore(x, y)

        for i in range(max(m, n)):
            if i < m and board[i][0] == "O":
                explore(i, 0)
            if i < m and board[i][n - 1] == "O":
                explore(i, n - 1)
            if i < n and board[0][i] == "O":
                explore(0, i)
            if i < n and board[m - 1][i] == "O":
                explore(m - 1, i)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

