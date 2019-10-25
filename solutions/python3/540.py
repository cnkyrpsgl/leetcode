class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if mid+1<len(nums) and nums[mid] == nums[mid+1]:
                if mid % 2 == 0: left = mid+2
                else: right = mid-1
            elif mid-1>=0 and nums[mid] == nums[mid-1]:
                if mid % 2 == 0: right = mid-2
                else: left = mid+1
            else: return nums[mid]
                