class Solution:
    def wiggleSort(self, nums):
        n = len(nums)
        for i in range(0, n -1, 2):
            if i == n - 2:
                if nums[-1] < nums[-2]:
                    nums[-2], nums[-1] = nums[-1], nums[-2]
            else:
                if nums[i + 2] >= nums[i + 1] < nums[i]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                elif nums[i] > nums[i + 2] <= nums[i + 1]:
                    nums[i], nums[i + 2] = nums[i + 2], nums[i]
                if nums[i + 2] > nums[i + 1]:
                    nums[i + 1], nums[i + 2] = nums[i + 2], nums[i + 1]    