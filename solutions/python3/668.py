class Solution:
    def findKthNumber(self, m, n, k):       
        l, r = 1, m * n
        while l < r:
            mid = (l + r) // 2
            if sum(min(mid // i, n) for i in range(1, m + 1)) < k:
                l = mid + 1
            else:
                r = mid
        return l