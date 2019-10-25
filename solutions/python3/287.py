class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low, high, mid = 0, len(nums)-1, len(nums)-1 // 2
        while high - low > 1:
            count, mid = 0, (high + low) // 2
            for k in nums:
                if mid < k <= high: count += 1
            if count > high - mid: low = mid
            else: high = mid
        return high