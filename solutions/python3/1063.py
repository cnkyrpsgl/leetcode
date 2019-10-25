class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack, res = [], 0
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            stack.append(num)
            res += len(stack)
        return res