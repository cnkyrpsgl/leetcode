class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        heap = [(0, 1)]
        visited = [0] * (N + 1)
        res = 0
        graph = [[] for _ in range(N + 1)]
        for a, b, c in connections:
            graph[a].append([b, c])
            graph[b].append([a, c])
        while heap:
            cost, city = heapq.heappop(heap)
            if visited[city]: continue
            visited[city] = 1
            res += cost
            for nCity, nCost in graph[city]:
                if not visited[nCity]:
                    heapq.heappush(heap, (nCost, nCity))
        return res if all(visited[1:]) else -1
            
            