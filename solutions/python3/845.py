class Solution:
    def longestMountain(self, A, res = 0):
        for i in range(1, len(A) - 1):
            if A[i + 1] < A[i] > A[i - 1]:
                l = r = i
                while l and A[l] > A[l - 1]: l -= 1
                while r + 1 < len(A) and A[r] > A[r + 1]: r += 1
                if r - l + 1 > res: res = r - l + 1
        return res