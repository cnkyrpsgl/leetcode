class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        flight = collections.defaultdict(list)
        for s, e, p in flights:
            flight[s].append((e, p))
        heap = [(0, src, K + 1)]
        while heap:
            price, city, stop = heapq.heappop(heap)
            if city == dst:
                return price
            elif stop > 0:
                for c, p in flight[city]:
                    heapq.heappush(heap, (price + p, c, stop - 1))
        return -1