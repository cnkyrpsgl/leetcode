class Solution:
    def findMaximizedCapital(self, k, W, Profits, Capital):
        pool, new = [], [(c, p) for c, p in zip(Capital, Profits)]
        heapq.heapify(new)
        for i in range(k):
            while new and new[0][0] <= W:
                c, p = heapq.heappop(new)
                heapq.heappush(pool, -p)
            try:
                p = -heapq.heappop(pool)
                W += p
            except:
                break
        return W