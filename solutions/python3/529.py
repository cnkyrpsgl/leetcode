class Solution(object):
    def updateBoard(self, board, click):
        def explore(i, j):
            visited.add((i, j))
            if board[i][j] == "M": board[i][j] = "X"
            else:
                points = ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j + 1), (i + 1, j - 1))
                cnt, adj = 0, []
                for p in points:
                    if 0 <= p[0] < m and 0 <= p[1] < n:
                        if board[p[0]][p[1]] == "M": cnt += 1
                        elif p not in visited: adj += p,
                if cnt == 0:
                    board[i][j] = "B"
                    for p in adj: explore(p[0], p[1])
                else: board[i][j] = str(cnt)
        m, n, visited = len(board), len(board and board[0]), set()
        explore(click[0], click[1])
        return board