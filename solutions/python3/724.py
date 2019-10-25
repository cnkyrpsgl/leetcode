class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sm = sum(nums)
        cur = 0
        for i in range(len(nums)):
            if cur == sm - cur - nums[i]:
                return i
            cur += nums[i]
        return -1