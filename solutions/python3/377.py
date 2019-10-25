class Solution:
    def combinationSum4(self, nums, target):
        memo = {}
        def dfs(sm):
            if sm in memo:
                return memo[sm]
            else:
                if sm >= target:
                    memo[sm] = sm == target
                    return memo[sm]
                cnt = 0
                for num in nums:
                    memo[sm + num] = dfs(sm + num)
                    cnt += memo[sm + num]
                return cnt          
        return dfs(0)