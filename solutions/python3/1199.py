class Solution:
    def minBuildTime(self, A: List[int], split: int) -> int:
        heapq.heapify(A)
        while len(A) > 1:
            x, y = heapq.heappop(A), heapq.heappop(A)
            heapq.heappush(A, y + split)
        return heapq.heappop(A)