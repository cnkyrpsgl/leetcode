class Solution:
    def threeSumClosest(self, nums, target):
        res = diff = float("inf")
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if abs(sm - target) < diff: diff, res = abs(sm - target), sm 
                if sm < target: l += 1
                elif sm > target: r -= 1
                else: return res
        return res