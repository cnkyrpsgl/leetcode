class Solution:
    def fourSum(self, nums, target):
        res, res_set = [], set()
        nums.sort()
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for j in range(i + 1, len(nums)):
                l, r = j + 1, len(nums) - 1
                while l < r:
                    sm = nums[i] + nums[j] + nums[l] + nums[r] 
                    if sm < target: l += 1
                    elif sm > target: r -= 1
                    elif (nums[i], nums[j], nums[l], nums[r]) not in res_set:
                        res.append([nums[i], nums[j], nums[l], nums[r]]); res_set.add((nums[i], nums[j], nums[l], nums[r])) 
                    else: l, r = l + 1, r - 1
        return res