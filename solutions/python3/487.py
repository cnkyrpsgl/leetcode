class Solution:
    def findMaxConsecutiveOnes(self, nums):
        l, zero, mx = 0, -1, 0
        for r, num in enumerate(nums + [0]):
            if not num:
                l, zero, mx = zero + 1, r, max(mx, r - l)
        return mx