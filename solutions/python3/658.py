class Solution:
    def findClosestElements(self, arr, k, x):
        ind, n = bisect.bisect_left(arr, x), len(arr)
        if ind > 0 and x - arr[ind - 1] < arr[ind] - x: ind -= 1
        l, r = ind, ind + 1
        for _ in range(k - 1):
            if r >= n or (l > 0 and x - arr[l - 1] <= arr[r] - x): l -= 1
            else: r += 1
        return arr[l:r]