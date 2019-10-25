class Solution:
    def minRefuelStops(self, target, startFuel, stations):
        q, n, memo = [(0, -startFuel, 0, 0)], len(stations), set()
        while q:
            refill, fuel, pos, index = heapq.heappop(q)
            fuel *= -1
            if index == n:
                if fuel - (target - pos) >= 0:
                    return refill
            else:
                sPos, add = stations[index]
                if (index, refill) not in memo and fuel - (sPos - pos) >= 0:
                    memo.add((index, refill))
                    f1 = (fuel - (sPos - pos) + add) * -1
                    f2 = (fuel - (sPos - pos)) * -1
                    heapq.heappush(q, (refill + 1, f1, sPos, index + 1))
                    heapq.heappush(q, (refill, f2, sPos, index + 1))
        return -1