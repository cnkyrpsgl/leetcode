class Solution:
    def subarraySum(self, nums, k):
        sums, res, sm = {}, 0, 0
        for i in range(len(nums)):
            sums[sm], sm = sm in sums and sums[sm] + 1 or 1, sm + nums[i]
            if sm - k in sums: res += sums[sm - k]
        return res