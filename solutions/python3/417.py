class Solution:
    def pacificAtlantic(self, matrix):
        pac, atl, m, n = set(), set(), len(matrix), len(matrix and matrix[0])
        def explore(i, j, ocean): 
            ocean.add((i, j))
            if i > 0 and (i - 1, j) not in ocean and matrix[i - 1][j] >= matrix[i][j]: explore(i - 1, j, ocean)
            if j > 0 and (i, j - 1) not in ocean and matrix[i][j - 1] >= matrix[i][j]: explore(i, j - 1, ocean)
            if i + 1 < m  and (i + 1, j) not in ocean and matrix[i + 1][j] >= matrix[i][j]: explore(i + 1, j, ocean)
            if j + 1 < n  and (i, j +1) not in ocean and matrix[i][j + 1] >= matrix[i][j]: explore(i, j + 1, ocean)
        for i in range(max(m, n)):
            if i < m and (i, 0) not in pac: explore(i, 0, pac)
            if i < n and (0, i) not in pac: explore(0, i, pac)
            if i < n and (m - 1, i) not in atl: explore(m - 1, i, atl)
            if i < m and (i, n - 1) not in atl: explore(i, n - 1, atl)
        return [[x, y] for x, y in pac & atl]