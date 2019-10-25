class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [x for x in set([i for i in range(1,len(nums)+1)])-set(nums)]