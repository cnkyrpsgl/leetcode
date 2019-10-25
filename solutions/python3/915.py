class Solution:
    def partitionDisjoint(self, A):
        rMin, lMax, mx, mn = [0] * len(A), [0] * len(A), -float("inf"), float("inf")
        for i, num in enumerate(A):
            mx = max(mx, num)
            lMax[i] = mx 
        for i in range(len(A) - 1, -1, -1):
            mn = min(mn, A[i])
            rMin[i] = mn 
        for i in range(len(A) - 1):
            if lMax[i] <= rMin[i + 1]:
                return i + 1