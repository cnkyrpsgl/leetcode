class Solution:
    def largestDivisibleSubset(self, nums):
        dp, n = [[num] for num in sorted(nums)], len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if not dp[j][-1] % dp[i][-1] and len(dp[i]) >= len(dp[j]):
                    dp[j] = dp[i] + dp[j][-1:]
        return dp and sorted(dp, key = len)[-1]