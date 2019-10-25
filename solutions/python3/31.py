class Solution:
    def nextPermutation(self, nums):
        perm, l = False, len(nums) - 2
        while 0 <= l:
            r = len(nums) - 1  
            while l < r and nums[r] <= nums[l]: 
                r -= 1
            if r <= l: 
                l -= 1
            else:
                nums[l], nums[l + 1:], perm = nums[r], sorted(nums[l + 1:r] + [nums[l]] + nums[r + 1:]), True
                break
        if not perm: nums.sort()