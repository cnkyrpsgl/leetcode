class Solution:
    def countSmaller(self, nums):
        r = []
        for i in range(len(nums) - 1, -1, -1):
            bisect.insort(r, nums[i])
            nums[i] = bisect.bisect_left(r, nums[i])
        return nums