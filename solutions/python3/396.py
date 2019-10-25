class Solution:
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        mx, sm = 0, sum(A)
        for i in range(len(A)):
            mx += i * A[i]
        curr = mx
        for i in range(1, len(A)):
            curr = curr - sm + A[i - 1] * len(A)
            mx = max(mx, curr)
        return mx