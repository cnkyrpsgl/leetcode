class Solution:
    def regionsBySlashes(self, grid):
        def dfs(i, j, k):
            if 0 <= i < n > j >= 0 and not matrix[i][j][k]:
                if grid[i][j] == "*":
                    if k <= 1:
                        matrix[i][j][0] = matrix[i][j][1] = cnt
                        dfs(i - 1, j, 2)
                        dfs(i, j + 1, 3)
                    else:
                        matrix[i][j][2] = matrix[i][j][3] = cnt
                        dfs(i + 1, j, 0)
                        dfs(i, j - 1, 1)
                elif grid[i][j] == "/":
                    if 1 <= k <= 2:
                        matrix[i][j][1] = matrix[i][j][2] = cnt
                        dfs(i, j + 1, 3)
                        dfs(i + 1, j, 0)
                    else:
                        matrix[i][j][0] = matrix[i][j][3] = cnt
                        dfs(i - 1, j, 2)
                        dfs(i, j - 1, 1)
                else:
                    matrix[i][j][0] = matrix[i][j][1] = matrix[i][j][2] = matrix[i][j][3] = cnt
                    dfs(i - 1, j, 2)
                    dfs(i, j + 1, 3)
                    dfs(i + 1, j, 0)
                    dfs(i, j - 1, 1)
        grid, n = [row.replace("\u005C\u005C", "*") for row in grid], len(grid)
        matrix, cnt = [[[0, 0, 0, 0] for j in range(n)] for i in range(n)], 0
        for i in range(n):
            for j in range(n):
                for k in range(4):
                    if not matrix[i][j][k]:
                        cnt += 1
                        dfs(i, j, k)
        return cnt