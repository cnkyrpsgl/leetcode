class Solution:
    def isIdealPermutation(self, A):
        for i, num in enumerate(A):
            if not (i - 1 <= num <= i + 1): return False
        return True