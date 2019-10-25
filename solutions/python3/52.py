class Solution:
    def totalNQueens(self, n):
        res = [0] 
        def dfs(i, l, r, m):
            if i == n: 
                res[0] += 1
            else:
                l = l[1:] + [0]
                r = [0] + r[:-1]
                for j in range(n):
                    if m[j] == l[j] == r[j] == 0:
                        l[j] = r[j] = m[j] = 1 
                        dfs(i + 1, l, r, m)
                        l[j] = r[j] = m[j] = 0
        dfs(0, [0] * n, [0] * n, [0] * n)
        return res[0]