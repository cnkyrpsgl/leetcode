class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target: 
                return mid
            elif sum((target < nums[l], nums[l] <= nums[mid], nums[mid] < target)) == 2: 
                l = mid + 1
            else: 
                r = mid - 1
        return -1