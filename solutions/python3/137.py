class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return ((sum(set(nums)) * 3) - sum(nums)) // 2