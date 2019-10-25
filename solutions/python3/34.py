class Solution(object):
    def searchRange(self, nums, target):
        l, r = bisect.bisect_left(nums, target), bisect.bisect_right(nums, target) - 1
        return [l, r] if 0 <= l <= r else [-1, -1]