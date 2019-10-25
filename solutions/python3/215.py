class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]