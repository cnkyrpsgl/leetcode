class Solution:
    def jump(self, nums):
        last = cur = jump = i = 0
        while cur < len(nums) - 1:
            while i <= last:
                if i + nums[i] > cur: cur = i + nums[i]
                i += 1
            last = cur
            jump += 1
        return jump