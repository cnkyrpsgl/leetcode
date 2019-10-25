class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks) != 1:
            new = heapq.heappop(sticks) + heapq.heappop(sticks)
            res += new
            heapq.heappush(sticks, new)
        return res
        