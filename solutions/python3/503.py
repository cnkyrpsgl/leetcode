class Solution:
    def nextGreaterElements(self, nums):
        stack, res = [], [-1] * len(nums)
        for j in range(2):
            for i in range(len(nums)):
                while stack and (nums[stack[-1]] < nums[i]): res[stack.pop()] = nums[i]
                if j == 1 and not stack: break
                stack += i, 
        return res