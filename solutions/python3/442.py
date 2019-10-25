class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out=list()
        for i in range(len(nums)):
            if nums[abs(nums[i])-1]<0: out.append(abs(nums[i]))
            else: nums[abs(nums[i])-1]*=-1
        return out