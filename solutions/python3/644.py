class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def sub(mid):
            sm = pre = mn = 0
            for i in range(k):
                sm += nums[i] - mid
            if sm >= 0:
                return True
            for i in range(k, len(nums)):
                sm += nums[i] - mid
                pre += nums[i - k] - mid
                mn = min(mn, pre)
                if sm >= mn:
                    return True
            return False
        l, r = min(nums), max(nums)
        while l + 1E-6 < r:
            mid = (l + r) / 2
            if sub(mid):
                l = mid
            else:
                r = mid
        return l