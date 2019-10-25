class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sm=sum(nums[:k])
        mx,j=sm/k, 0
        for i in range(k,len(nums)): sm+=nums[i]; sm-=nums[j]; curr=sm/k; mx=max(curr,mx); j+=1
        return mx