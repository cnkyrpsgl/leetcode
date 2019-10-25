class Solution:
    def threeSum(self, nums):
        res, res_set = [], set()
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r] 
                if sm < 0: l += 1
                elif sm > 0: r -= 1
                elif (nums[i], nums[l], nums[r]) not in res_set: 
                    res.append([nums[i], nums[l], nums[r]])
                    res_set.add((nums[i], nums[l], nums[r])) 
                else: l, r = l + 1, r - 1
        return res