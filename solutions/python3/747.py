class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx = max(nums)
        return nums.index(mx) if all(num * 2 <= mx for num in nums if num < mx) else -1