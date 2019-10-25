class Solution:
    def maxSubArrayLen(self, nums, k):
        index, l, sm = {}, 0, 0
        index[0] = -1
        for i, num in enumerate(nums):
            sm += num
            if sm - k in index:
                l = max(l, i - index[sm - k])
            if sm not in index:
                index[sm] = i
        return l