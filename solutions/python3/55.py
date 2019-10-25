class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = mx = 0
        while i < len(nums) and i <= mx:
            if nums[i] + i >= len(nums) - 1: return True
            mx, i = max(mx, i + nums[i]), i + 1
        return False