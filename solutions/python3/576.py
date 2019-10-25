class Solution:
    def __init__(self): self.dic = collections.defaultdict(int)
    def findPaths(self, m, n, N, i, j):
        if N >= 0 and (i < 0 or j < 0 or i >= m or j >= n): return 1
        elif N < 0: return 0
        elif (i, j, N) not in self.dic: 
            for p in ((1, 0), (-1, 0), (0, 1), (0, -1)): self.dic[(i, j, N)] += self.findPaths(m, n, N - 1, i + p[0], j + p[1]) 
        return self.dic[(i, j, N)] % (10 ** 9 + 7) 