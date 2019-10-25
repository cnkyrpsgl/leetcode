class Solution:
    def findNumberOfLIS(self, nums):
        dp = [[1, 1] for _ in range(len(nums))]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    if dp[i][0] >= dp[j][0]: dp[j] = [dp[i][0] + 1, dp[i][1]]
                    elif dp[i][0] == dp[j][0] - 1: dp[j][1] += dp[i][1]
        dp.sort()
        return dp and sum(d[1] for d in dp if d[0] == dp[-1][0]) or 0