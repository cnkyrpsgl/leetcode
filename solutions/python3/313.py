class Solution:
    def nthSuperUglyNumber(self, n, primes):
        arr, heap, used = [1], primes[:], set()
        for i in range(1, n):
            num = heapq.heappop(heap)
            arr.append(num)
            for p in primes:
                if p * num not in used:
                    heapq.heappush(heap, p * num)
                    used.add(p * num)
        return arr[-1]