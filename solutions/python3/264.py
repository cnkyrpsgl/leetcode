class Solution:
    def nthUglyNumber(self, n):
        arr, heap, used = [], [1], set()
        for i in range(n):
            num = heapq.heappop(heap)
            arr.append(num)
            for p in (2, 3, 5):
                if p * num not in used:
                    heapq.heappush(heap, p * num)
                    used.add(p * num)
        return arr[-1]