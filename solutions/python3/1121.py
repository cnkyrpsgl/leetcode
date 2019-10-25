class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        return K * max(collections.Counter(nums).values()) <= len(nums)              