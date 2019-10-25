class Solution:
    def maxDistance(self, arrays):
        arrays.sort(key = lambda x: x[0])
        d1 = max(arr[-1] for arr in arrays[1:]) - arrays[0][0]
        arrays.sort(key = lambda x: x[-1])
        d2 = arrays[-1][-1] - min(arr[0] for arr in arrays[:-1])
        return max(d1, d2)