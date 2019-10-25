class Solution:
    def findWords(self, board, words):
        def explore(i, j, cur):
            visited[i][j] = 0
            if "#" in cur and cur["#"] not in res_set: res.append(cur["#"]); res_set.add(cur["#"])
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and board[x][y] in cur and visited[x][y] == -1: explore(x, y, trie[cur[board[x][y]]])
            visited[i][j] = -1
        trie, cnt, m, n, res, res_set = {}, 1, len(board), len(board and board[0]), [], set()
        visited, trie[0] = [[-1] * n for _ in range(m)], {}
        for w in words:
            cur = trie[0]
            for c in w:
                if c not in cur: trie[cnt], cur[c], cnt = {}, cnt, cnt + 1
                cur = trie[cur[c]]
            cur["#"] = w
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie[0]: explore(i, j, trie[trie[0][board[i][j]]])
        return res