class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False
        d = {}
        for i in range(len(nums)):
            m = nums[i] // (t + 1)
            if m in d or (m - 1 in d and nums[i] - d[m - 1] <= t) or (m + 1 in d and d[m + 1] - nums[i] <= t):
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] // (t + 1)]
        return False