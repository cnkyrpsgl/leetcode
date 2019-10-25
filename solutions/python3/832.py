class Solution(object):
    def flipAndInvertImage(self, A):
        return [[1 - x for x in A[i][::-1]] for i in range(len(A))]