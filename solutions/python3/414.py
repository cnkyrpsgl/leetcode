class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=list(set(nums))
        if s[-1]<s[0]: s=[item for item in s if item>=0]
        if len(s)>=3: return s[-3]
        else: return s[-1] 