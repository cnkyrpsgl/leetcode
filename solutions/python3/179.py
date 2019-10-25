class Solution:
    def largestNumber(self, nums):
        def partition(l, r):
            j = l
            for i in range(l + 1, r + 1):
                if nums[i] + nums[l] >= nums[l] + nums[i]:
                    j += 1
                    nums[j], nums[i] = nums[i], nums[j]
            nums[l], nums[j] = nums[j], nums[l]
            return j
        def quickSort(l, r):
            if l < r:
                m = partition(l, r)
                quickSort(l, m - 1)
                quickSort(m + 1, r)
        nums = [str(num) for num in nums]
        quickSort(0, len(nums) - 1)  
        return str(int("".join(nums)))