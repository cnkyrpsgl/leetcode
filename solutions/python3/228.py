class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res, stack = [], [nums[0] if nums else None, None]
        for i, num in enumerate(nums):
            if i > 0 and nums[i - 1] == num - 1: stack[1] = num
            if i > 0 and nums[i-1] != num - 1: res, stack[0], stack[1] = res + ["->".join(str(q) for q in stack if q != None)], num, None
            if i == len(nums) - 1: res.append("->".join(str(q) for q in stack if q != None))
        return res