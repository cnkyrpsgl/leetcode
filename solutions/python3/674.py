class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]: return 0
        curr, mx=1, 1
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]: curr+=1; mx=max(mx,curr)
            else: curr=1
        return mx