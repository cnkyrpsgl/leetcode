class Solution(object):
    def threeEqualParts(self, A):
        sm = sum(A)
        if sm % 3: return [-1, -1]
        t = sm // 3
        if not t: return [0, len(A) - 1]
        breaks = [0] + [i for i, x in enumerate(A) if x]
        i1, j1, i2, j2, i3, j3 = breaks[1], breaks[t], breaks[t + 1], breaks[2 * t], breaks[2 * t + 1], breaks[3 * t]
        if not (A[i1: j1 + 1] == A[i2: j2 + 1] == A[i3: j3 + 1]): return [-1, -1]
        if i2 - j1 < len(A) - j3 or i3 - j2 < len(A) - j3: return [-1, -1]
        return [j1 + len(A) - j3 - 1, j2+ len(A) - j3]