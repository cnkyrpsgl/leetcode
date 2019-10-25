class Solution:
    def increasingTriplet(self, nums):
        mn = None
        for i in range(len(nums)):
            if mn == None or nums[i] < mn: 
                mn = nums[i]
            if mn < nums[i]:
                nums[i] = [True, nums[i]]
            else:
                nums[i] = [False, nums[i]]
        mn = None
        for i in range(len(nums)):
            if nums[i][0] and (mn == None or nums[i][1] < mn):
                mn = nums[i][1]
            elif mn != None and mn < nums[i][1]:
                return True
        return False 