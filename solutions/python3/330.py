class Solution:
    def minPatches(self, nums, n):
        miss, added, i = 1, 0, 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss *= 2
                added += 1
        return added