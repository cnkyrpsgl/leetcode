class Solution:
    def maxSlidingWindow(self, nums, k):
        cnt, heap, res = collections.Counter(), [], []
        for i, num in enumerate(nums):
            heapq.heappush(heap, -num)
            cnt[num] += 1
            while not cnt[-heap[0]]:
                heapq.heappop(heap)
            if i >= k - 1:
                res.append(-heap[0])
                cnt[nums[i - k + 1]] -= 1
        return res