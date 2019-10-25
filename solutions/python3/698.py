class Solution:
    def canPartitionKSubsets(self, nums, k):
        def dfs(i, sums):
            if i == n:
                return True
            for j in range(k):
                if sums[j] + nums[i] <= target:
                    sums[j] += nums[i]
                    if dfs(i + 1, sums):
                        return True
                    sums[j] -= nums[i]
            return False
        nums.sort(reverse = True)
        sm = sum(nums)
        if sm % k: return False
        target, n = sm // k, len(nums)
        return dfs(0, [0] * k)