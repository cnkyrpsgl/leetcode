class Solution:
    def checkSubarraySum(self, nums, k):
        if not k: return any(nums[i] == nums[i - 1] == 0 for i in range(1, len(nums)))
        mods, sm = set(), 0
        for i, num in enumerate(nums):
            sm = (sm + num) % k
            if (sm in mods and num or (i and not nums[i - 1])) or (not sm and i): return True
            mods |= {sm}
        return False