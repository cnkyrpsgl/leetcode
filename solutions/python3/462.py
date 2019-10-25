class Solution:
    def minMoves2(self, nums):
        nums.sort()
        m = nums[(len(nums) - 1) // 2] 
        return sum(abs(num - m) for num in nums)