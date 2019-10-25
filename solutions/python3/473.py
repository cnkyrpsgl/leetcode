class Solution:
    def makesquare(self, nums):
        def dfs(index, edge, count, used):
            for i in range(index, len(nums)):
                if i in used or edge - nums[i] < 0: continue
                elif edge - nums[i] > 0 and dfs(i + 1, edge - nums[i], count, used | {i}): return True
                elif edge - nums[i] == 0 and (count and dfs(1, l, count - 1, used | {i})) or not count: return True
            return False
        sm = sum(nums)
        if len(nums) < 4 or sm % 4 != 0: return False
        l = sm // 4 
        nums.sort(reverse = True)
        if nums[0] > l: return False
        return nums[0] == l and dfs(1, l, 1, {0}) or dfs(1, l - nums[0], 2, {0})