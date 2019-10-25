class Solution:
    def distanceBetweenBusStops(self, d: List[int], i: int, j: int) -> int:
        return min(sum(d[min(i, j):max(i, j)]), sum(d[:min(i, j)] + d[max(i, j):]))