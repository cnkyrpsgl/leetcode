class Solution:
    def deleteAndEarn(self, nums):
        cnt, dp, maxs = collections.Counter(nums), {}, {}
        nums = sorted(set(nums))
        if len(nums) < 2:
            return nums and nums[0] * cnt[nums[0]] or 0
        for i in range(len(nums)):
            dp[i] = nums[i] * cnt[nums[i]]
            if i >= 2:
                if nums[i - 1] < nums[i] - 1:
                    dp[i] += maxs[i - 1]
                else:
                    dp[i] += maxs[i - 2]
                maxs[i] = max(dp[i], maxs[i - 1])
            elif i:
                if nums[i - 1] < nums[i] - 1:
                    dp[i] += dp[i - 1]
                maxs[i] = max(dp[i], dp[i - 1])
            else:
                maxs[i] = dp[i]
        return max(dp[len(nums) - 1], dp[len(nums) - 2])