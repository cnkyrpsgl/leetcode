class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def check(mx):
            days, cur = 1, 0
            for w in weights:
                if cur + w <= mx:
                    cur += w
                else:
                    days += 1
                    cur = w
            return days
            
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            days = check(mid)
            if days <= D:
                r = mid
            else:
                l = mid + 1
        return r