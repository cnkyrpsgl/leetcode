class Solution:
    def minSubArrayLen(self, s, nums):
        l, res, curr = 0, len(nums) + 1, 0
        for r, num in enumerate(nums):
            curr += num
            while curr >= s: res, l, curr = min(res, r - l + 1), l + 1, curr - nums[l]
        return res < len(nums) + 1 and res or 0