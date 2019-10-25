class Solution:
    def shortestSubarray(self, A, K):
        heap, l, sm = [], float("inf"), 0
        heapq.heappush(heap, (0, -1))
        for i, num in enumerate(A):
            sm += num
            dif = sm - K
            while heap and (heap[0][0] <= dif or i - heap[0][1] >= l):
                preSum, preIndex = heapq.heappop(heap)
                if i - preIndex < l:
                    l = i - preIndex
            heapq.heappush(heap, (sm, i))
        return l < float("inf") and l or -1