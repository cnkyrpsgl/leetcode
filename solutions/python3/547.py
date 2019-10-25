class Solution:
    def findCircleNum(self, m):
        res, n = 0, len(m)
        def explore(i):
            m[i][i] = 0
            for j in range(n):
                if i != j and m[i][j] == m[j][j] == 1: explore(j)
        for i in range(n):
            if m[i][i] == 1: explore(i); res += 1
        return res