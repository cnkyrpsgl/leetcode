class Solution:
    def kthSmallest(self, matrix, k):
        return sorted(itertools.chain(*matrix))[k - 1]