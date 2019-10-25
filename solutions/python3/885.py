class Solution:
    def spiralMatrixIII(self, R, C, r0, c0):
        direct, res, n, l, ind = [(-1, 0), (0, 1), (1, 0), (0, -1)], [[r0, c0]], R * C, 1, 1
        while len(res) < n:
            for __ in range(2):
                for _ in range(l):
                    r0 += direct[ind][0]
                    c0 += direct[ind][1]
                    if 0 <= r0 < R and 0 <= c0 < C:
                        res.append([r0, c0])
                ind = (ind + 1) % 4
            l += 1
        return res