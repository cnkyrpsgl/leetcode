class Solution(object):
    def countPairsLTE(self, array, value):
        return sum(bisect.bisect_right(array, array[i] + value, lo = i) - i - 1 for i in range(len(array)))
        
    def smallestDistancePair(self, nums, k):
        nums.sort()
        low, high = min([nums[i + 1] - nums[i] for i in range(len(nums) - 1)]), nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if self.countPairsLTE(nums, mid) < k:
                low = mid + 1
            else:
                high = mid
        return low