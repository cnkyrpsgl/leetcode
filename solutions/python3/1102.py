class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        heap = [(-A[0][0], 0, 0)]
        res = A[0][0]
        m, n = len(A), len(A[0])
        while heap:
            val, i, j = heapq.heappop(heap)
            A[i][j] = -1
            res = min(res, -val)
            if i == m - 1 and j == n - 1:
                break
            for x, y in (i + 1, j) , (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < m and 0 <= y < n and A[x][y] >= 0:
                    heapq.heappush(heap, (-A[x][y], x, y))
        return res
            