class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [n[0] for n in collections.Counter(nums).most_common()[-2:]]