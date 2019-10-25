class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        res, start, diff = 0, -1, 0
        for i in range (len(A)):
            if L <= A[i] <= R: diff, res = i - start, res + i - start
            elif A[i] > R: diff, start = 0, i
            else: res += diff
        return res