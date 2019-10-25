class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        l, res, cur = 0, 0, 1
        for i in range(len(nums)):
            cur *= nums[i]
            while cur >= k and l < i: l, cur = l + 1, cur // nums[l]
            if cur < k: res += i - l + 1
        return res