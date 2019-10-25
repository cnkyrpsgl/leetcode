class Solution:
    
    def count(self, num):
        cnt = 0
        while num:
            cnt += num // 5
            num //= 5
        return cnt 
    
    def preimageSizeFZF(self, K):
        l, r = 0, 2 ** 63 - 1
        while l < r:
            mid = (l + r) // 2
            if self.count(mid) < K:
                l = mid + 1
            else:
                r = mid
        return 5 - (l % 5) if self.count(l) == K else 0