class Solution:
    def longestConsecutive(self, nums):
        res, items = 0, set(nums)
        for num in items:
            if num - 1 not in items:
                cur = 1
                while num + 1 in items:
                    num, cur = num + 1, cur + 1   
                if cur > res: res = cur
        return res