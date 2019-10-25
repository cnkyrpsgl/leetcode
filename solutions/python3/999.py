class Solution:
    def numRookCaptures(self, board: List[List[str]], res = 0) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    for x in range(i - 1, -1, -1):
                        if board[x][j] in 'Bp':
                            res += board[x][j] == 'p'
                            break
                    for x in range(i + 1, 8):
                        if board[x][j] in 'Bp':
                            res += board[x][j] == 'p'
                            break
                    for y in range(j - 1, -1, -1):
                        if board[i][y] in 'Bp':
                            res += board[i][y] == 'p'
                            break
                    for y in range(j + 1, 8):
                        if board[i][y] in 'Bp':
                            res += board[i][y] == 'p'
                            break
                    return res