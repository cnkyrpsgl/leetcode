class Solution:
    def pathSum(self, nums):
        dp = {(0, 1) : 0}
        for num in nums:
            d, p, v = map(int, str(num))
            dp[(d, p)] = v + dp[(d - 1, (p + 1) // 2)]
        return sum(dp[k] for k in dp if (k[0] + 1, k[1] * 2) not in dp and (k[0] + 1, k[1] * 2 - 1) not in dp)