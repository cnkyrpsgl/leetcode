class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        single, double, sm, n, cur = {}, {}, 0, len(nums), sum(nums[:k - 1])
        for i in range(k - 1, n):
            cur += nums[i]
            single[i - k + 1] = cur
            cur -= nums[i - k + 1]
        cur = n - k, single[n - k]
        for i in range(n - k, k * 2 - 1, -1):
            if single[i] >= cur[1]:
                cur = i, single[i]
            double[i - k] = cur[1] + single[i - k], i - k, cur[0]
        cur = double[n - 2 * k]
        for i in range(n - 2 * k, k - 1, -1):
            if double[i][0] >= cur[0]:
                cur = double[i]
            if single[i - k] + cur[0] >= sm:
                sm, res = single[i - k] + cur[0], [i - k, cur[1], cur[2]]
        return res