class Solution:
    def findMin(self, nums):
        l, r, res = 0, len(nums) - 1, nums and nums[0]
        while l <= r:
            while l < r and nums[l] == nums[l + 1]: l += 1
            while l < r and nums[r] == nums[r - 1]: r -= 1
            mid = (l + r) // 2
            if nums[mid] >= nums[0]: l = mid + 1
            else: r, res = mid - 1, min(res, nums[mid])
        return res