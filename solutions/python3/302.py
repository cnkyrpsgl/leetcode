class Solution:
    def minArea(self, image, x, y):
        l, r, u, d, m, n = [y], [y], [x], [x], len(image), len(image[0])
        def dfs(i, j):
            if i < u[0]: u[0] = i
            elif i > d[0]: d[0] = i
            if j < l[0]: l[0] = j
            elif j > r[0]: r[0] = j
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and image[x][y] == "1":
                    image[x][y] = "0"
                    dfs(x, y)
        dfs(x, y)
        return (r[0] - l[0] + 1) * (d[0] - u[0] + 1)