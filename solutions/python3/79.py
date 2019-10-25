class Solution:
    def exist(self, board, word):
        m, n, o = len(board), len(board and board[0]), len(word)
        def explore(i, j, k, q):
            for x, y in ((i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)):
                if k>=o or (0<=x<m and 0<=y<n and board[x][y]==word[k] and (x,y) not in q and explore(x,y,k+1,q|{(x,y)})): return True
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and explore(i, j, 1, {(i, j)}): return True
        return False