class Solution:
    def shortestBridge(self, A):
        def dfs(i, j):
            A[i][j] = -1
            q.append((i, j))
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                    dfs(x, y)
        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return i, j
        n, step, q = len(A), 0, []
        dfs(*first())
        while True:
            new = []
            for i, j in q:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            new.append((x, y))
            step += 1
            q = new