class Solution:
    def maxSubArray(self, nums):
        sm, mn, mx = 0, 0, -float("inf")
        for num in nums:
            sm += num
            mx, mn = max(mx, sm - mn), min(mn, sm)
        return mx