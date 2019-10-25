class Solution:
    def PredictTheWinner(self, nums):
        def dfs(l, r, p1, p2, turn):
            if l > r:
                return p1 >= p2
            elif turn:
                return dfs(l + 1, r, p1 + nums[l], p2, 0) or dfs(l, r - 1, p1 + nums[r], p2, 0)
            else:
                return dfs(l + 1, r, p1, p2 + nums[l], 1) and dfs(l, r - 1, p1, p2 + nums[r], 1)
        return dfs(0, len(nums) - 1, 0, 0, 1)