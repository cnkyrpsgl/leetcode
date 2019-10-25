class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for a, b, c in trips:
            heapq.heappush(heap, (b, a))
            heapq.heappush(heap, (c, -a))
        cur = 0
        while heap:
            cur += heapq.heappop(heap)[1]
            if cur > capacity: return False
        return True