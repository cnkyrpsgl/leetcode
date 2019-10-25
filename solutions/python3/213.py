class Solution:
    
    def dp(self, nums):
        if len(nums) <= 2: return max(nums or [0])
        nums[2] += nums[0]
        for i in range(3, len(nums)): nums[i] += max(nums[i - 2], nums[i - 3])
        return max(nums[-1], nums[-2])
    
    def rob(self, nums):
        return max(self.dp(nums[:-1]), self.dp(nums[1:])) if len(nums) != 1 else nums[0]