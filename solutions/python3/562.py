class Solution:
    def longestLine(self, M):
        hor, ver, dig, aDig, mx, m, n = {}, {}, {}, {}, 0, len(M), len(M and M[0])
        for i in range(m):
            for j in range(n):
                if M[i][j]:
                    ver[(i, j)] = j > 0 and M[i][j - 1] and ver[(i, j - 1)] + 1 or 1
                    hor[(i, j)] = i > 0 and M[i - 1][j] and hor[(i - 1, j)] + 1 or 1
                    dig[(i, j)] = i > 0 and j > 0 and M[i - 1][j - 1] and dig[(i - 1, j - 1)] + 1 or 1
                    aDig[(i, j)] = i > 0 and j + 1 < n and M[i - 1][j + 1] and aDig[(i - 1, j + 1)] + 1 or 1
                    mx = max(mx, ver[(i, j)], hor[(i, j)], dig[(i, j)], aDig[(i, j)])
        return mx