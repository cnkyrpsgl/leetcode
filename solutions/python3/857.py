class Solution:
    def mincostToHireWorkers(self, quality, wage, K):
        workers, res, heap, sumq = sorted((w / q, q, w) for q, w in zip(quality, wage)), float("inf"), [], 0
        for ratio, q, w in workers:
            heapq.heappush(heap, -q)
            sumq += q
            if len(heap) > K:
                sumq += heapq.heappop(heap)
            if len(heap) == K:
                res = min(res, ratio * sumq)
        return res