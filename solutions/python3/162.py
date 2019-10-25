class Solution:
    def findPeakElement(self, nums):
        l, r, n = 0, len(nums) - 1, len(nums)
        while l <= r:
            mid = (l + r) // 2
            pre, after = mid == 0 and -float("inf") or nums[mid - 1], mid == n - 1 and -float("inf") or nums[mid + 1]
            if pre < nums[mid] > after: return mid
            elif pre > nums[mid]: r = mid - 1
            else: l = mid + 1