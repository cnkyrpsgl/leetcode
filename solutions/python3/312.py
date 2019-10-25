class Solution:
    def maxCoins(self, nums):
        memo, nums = {}, [1] + [num for num in nums if num] + [1]
        def dfs(l, r):
            if r - l == 1: return 0
            if (l, r) not in memo: memo[(l, r)] = max(nums[l] * nums[i] * nums[r] + dfs(l, i) + dfs(i, r) for i in range(l + 1, r))
            return memo[(l, r)]
        return dfs(0, len(nums) - 1)