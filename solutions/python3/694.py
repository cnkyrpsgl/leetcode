class Solution:
    def numDistinctIslands(self, grid):
        visited, pattern, m, n = set(), collections.defaultdict(str), len(grid), len(grid[0])
        def dfs(ri, rj, i, j, pi, pj):
            visited.add((i, j))
            pattern[(ri, rj)] += str(pi) + str(pj)
            for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if 0 <= i + x < m and 0 <= j + y < n and grid[i + x][j + y] and (i + x, j + y) not in visited:
                    dfs(ri, rj, i + x, j + y, pi + x, pj + y)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited:
                    dfs(i, j, i, j, 0, 0)
        return len(set(pattern.values()))