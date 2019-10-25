from itertools import product as pr


class Solution(object):
    def findSolution(self, customfunction, z):
        return [
            [i, j]
            for i, j in pr(range(1, z + 1), repeat=2)
            if customfunction.f(i, j) == z
        ]

