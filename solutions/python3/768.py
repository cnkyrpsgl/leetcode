class Solution:
    def maxChunksToSorted(self, arr):
        mx, mn, res, check = 0, 10 ** 9, 0, [[0, 0] for _ in range(len(arr))]
        for i in range(len(arr)):
            if arr[i] > mx: mx = arr[i]
            check[i][0] = mx
        for i in range(len(arr) -1, -1, -1):
            check[i][1] = mn
            if arr[i] < mn: mn = arr[i]
        for c in check:
            if c[0] <= c[1]: res += 1
        return res