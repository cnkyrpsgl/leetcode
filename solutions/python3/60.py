class Solution:
    def getPermutation(self, n, k):
        p = itertools.permutations(range(1, n + 1))
        for i in range(k): 
            res = next(p)
        return ''.join([str(i) for i in res])