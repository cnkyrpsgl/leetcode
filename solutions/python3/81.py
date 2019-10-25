class Solution:
    def search(self, nums, target):
        l, r, n = 0, len(nums) - 1, len(nums)
        while l <= r:
            while l + 1 < n and nums[l + 1] == nums[l]: 
                l += 1
            while r > 0 and nums[r] == nums[r - 1]: 
                r -= 1
            mid = (l + r) // 2
            if nums[mid] == target: 
                return True
            elif sum((target < nums[l], nums[l] <= nums[mid], nums[mid] < target)) == 2: 
                l = mid + 1
            else: 
                r = mid - 1
        return False