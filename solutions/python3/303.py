class NumArray:

    def __init__(self, nums):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i - 1]
        

    def sumRange(self, i, j):
        return self.nums[j] - self.nums[i - 1] if i else self.nums[j]