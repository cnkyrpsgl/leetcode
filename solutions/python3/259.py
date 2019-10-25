class Solution:
    def threeSumSmaller(self, nums, target):
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            r = len(nums) - 1
            for j in range(i + 1, len(nums) - 1):
                while r > j + 1 and nums[i] + nums[j] + nums[r] >= target:
                    r -= 1
                if nums[i] + nums[j] + nums[r] < target:
                    res += r - j
        return res