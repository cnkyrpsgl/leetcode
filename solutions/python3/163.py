class Solution:
    def findMissingRanges(self, nums, lower, upper):
        if not nums:
            return [str(lower) + "->" + str(upper)] if lower != upper else [str(lower)]
        res, n = [], len(nums)
        if lower + 1 < nums[0]:
            res.append(str(lower) + "->" + str(nums[0] - 1))
        elif lower + 1 == nums[0]:
            res.append(str(lower))
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 2:
                res.append(str(nums[i] - 1))
            elif nums[i] > nums[i - 1] + 2:
                res.append(str(nums[i - 1] + 1) + "->" + str(nums[i] - 1))
        if nums[-1] + 1 < upper: 
            res.append(str(nums[-1] + 1) + "->" + str(upper))
        elif nums[-1] + 1 == upper:
            res.append(str(upper))
        return res