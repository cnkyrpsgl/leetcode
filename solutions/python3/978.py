class Solution:
    def maxTurbulenceSize(self, A):
        arr = [A[i - 1] < A[i] for i in range(1, len(A))]
        cur = mx = 1 + (len(A) > 1)
        for i in range(1, len(arr)):
            if A[i] != A[i + 1] and arr[i] != arr[i - 1]:
                cur += 1
                mx = max(cur, mx)
            else:
                cur = 2
        return mx