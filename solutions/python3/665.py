class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """  
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                mod1, mod2=list(nums), list(nums)
                mod1[i], mod2[i+1]=mod1[i+1], mod2[i]
                if mod1!=sorted(mod1) and mod2!=sorted(mod2): return False
        return True