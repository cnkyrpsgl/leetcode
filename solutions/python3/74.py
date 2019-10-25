class Solution:
    def searchMatrix(self, matrix, target):
        ls = list(itertools.chain(*matrix))
        return ls and ls[bisect.bisect(ls, target) - 1] == target or False