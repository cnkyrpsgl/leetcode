class Solution:
    def kthSmallestPrimeFraction(self, A, K):
        heap, used = [(A[0] / A[-1], 0, len(A) - 1)], {(0, len(A) - 1)}
        for i in range(K):
            try:
                cur, l, r = heapq.heappop(heap)
                used.add((l, r))
                if (l + 1, r) not in used:
                    heapq.heappush(heap, (A[l + 1] / A[r], l + 1, r))
                    used.add((l + 1, r))
                if (l, r - 1) not in used:
                    heapq.heappush(heap, (A[l] / A[r - 1], l, r - 1))
                    used.add((l, r - 1))
            except:
                break
        return [A[l], A[r]]