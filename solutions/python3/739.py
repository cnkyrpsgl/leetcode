class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        heap = []
        for j, t in enumerate(T):
            while heap and heap[0][0] < t:
                temp, i = heapq.heappop(heap)
                res[i] = j - i
            heapq.heappush(heap, (t, j))
        return res
        