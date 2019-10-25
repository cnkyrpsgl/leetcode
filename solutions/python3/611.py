class Solution:
    def triangleNumber(self, nums):
        res, n = 0, len(nums); nums.sort()
        for i in range(n - 1, 1, -1):
            j, k = i - 1, 0
            while k < j:
                if nums[j] + nums[k] > nums[i]: res, j = res + j - k, j - 1
                else: k += 1
        return res