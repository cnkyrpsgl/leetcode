class Solution:
    def maxProduct(self, nums):
        res, min_pos, max_neg, cur = -float("inf"), float("inf"), -float("inf"), 1
        for num in nums:
            cur *= num
            if cur > res: res = cur
            elif 0 < cur // min_pos > res: res = cur // min_pos
            elif 0 < cur // max_neg > res: res = cur // max_neg
            if cur == 0: min_pos, max_neg, cur = float("inf"), -float("inf"), 1
            elif max_neg < cur < 0: max_neg = cur
            elif 0 < cur < min_pos: min_pos = cur
        return res