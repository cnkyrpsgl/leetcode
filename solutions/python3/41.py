class Solution:
    def firstMissingPositive(self, nums: List[int], res: int = 1) -> int:
        for num in sorted(nums):
            res += num == res
        return res
        