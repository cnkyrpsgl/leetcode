class Solution:
    def largestIsland(self, grid):
        def explore(i, j):
            dic[(i, j)], count[curr] = curr, count[curr] + 1
            if i > 0 and grid[i - 1][j] == 1 and (i - 1, j) not in dic: explore(i - 1, j)
            if j > 0 and grid[i][j - 1] == 1 and (i, j - 1) not in dic: explore(i, j - 1)
            if i + 1 < len(grid) and grid[i + 1][j] ==1 and (i + 1, j) not in dic: explore(i + 1, j)
            if j + 1 < len(grid) and grid[i][j + 1] == 1 and (i, j + 1) not in dic: explore(i, j + 1)
        def neighbours(i, j, adj):
            if i > 0 and grid[i - 1][j] == 1 and dic[(i - 1, j)] not in adj: adj.add(dic[(i - 1, j)])
            if j > 0 and grid[i][j - 1] == 1 and dic[(i, j - 1)] not in adj: adj.add(dic[(i, j - 1)])
            if i + 1 < len(grid) and grid[i + 1][j] ==1 and dic[(i + 1, j)] not in adj: adj.add(dic[(i + 1, j)])
            if j + 1 < len(grid) and grid[i][j + 1] == 1 and dic[(i, j + 1)] not in adj: adj.add(dic[(i, j + 1)])
            return adj
        curr, dic, count, res = 0, {}, collections.defaultdict(int), 0
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1 and (i, j) not in dic: curr += 1; explore(i, j)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1: res = max(res, count[dic[(i, j)]])
                else: res = max(res, sum(count[r] for r in neighbours(i, j, set())) + 1)
        return res