class Solution:
    def hIndex(self, citations):
        l, r, res = 0, len(citations) - 1, 0
        while l <= r:
            mid = (l + r) // 2
            if len(citations) - mid <= citations[mid]: res, r = len(citations) - mid, r - 1
            else: l = mid + 1
        return res