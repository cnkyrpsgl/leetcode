class Solution:
    def candyCrush(self, board):
        m, n = len(board), len(board[0])
        def gravity():
            for j in range(n):
                stack = [board[i][j] for i in range(m - 1, -1, -1) if board[i][j] > 0]
                stack += [0] *  (m - len(stack))
                for i in range(m): board[i][j] = stack.pop()
        def crush():
            crush = False
            for i in range(m):
                for j in range(n):
                    if j > 1 and board[i][j] > 0 and board[i][j] == abs(board[i][j - 1]) == abs(board[i][j - 2]):
                        board[i][j - 2:j + 1] = [-abs(board[i][j]) for _ in range(3)]
                        crush = True
                    if i > 1 and board[i][j] != 0 and abs(board[i][j]) == abs(board[i - 1][j]) == abs(board[i - 2][j]):
                        if board[i][j] > 0: board[i][j] *= -1
                        if board[i - 1][j] > 0: board[i - 1][j] *= -1
                        if board[i - 2][j] > 0: board[i - 2][j] *= -1
                        crush = True
            return crush  
        while crush(): gravity()
        return board