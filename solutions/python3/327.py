class Solution:
    def countRangeSum(self, nums, lower, upper):
        sums, sm, res = [0], 0, 0
        for num in nums:
            sm += num
            res += bisect.bisect_right(sums, sm - lower) - bisect.bisect_left(sums, sm - upper)
            bisect.insort(sums, sm)
        return res