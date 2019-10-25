class Solution:
    def knightProbability(self, N, K, r, c):
        memo = {}
        def dfs(i, j, p, k): 
            if 0 <= i < N and 0 <= j < N and k < K:
                sm = 0
                for x, y in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2)):
                    if (i + x, j + y, k) not in memo:
                        memo[(i + x, j + y, k)] = dfs(i + x, j + y, p / 8, k + 1)
                    sm += memo[(i + x, j + y, k)]
                return sm
            else:
                return 0 <= i < N and 0 <= j < N and p or 0
        return dfs(r, c, 1, 0)