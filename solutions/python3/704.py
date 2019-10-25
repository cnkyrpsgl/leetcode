class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target) if target in nums else -1