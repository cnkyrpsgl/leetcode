class Solution:
    def shortestPathLength(self, graph):
        memo, final, q = set(), (1 << len(graph)) - 1, collections.deque([(i, 0, 1 << i) for i in range(len(graph))])
        while q:
            node, steps, state = q.popleft()
            if state == final: return steps
            for v in graph[node]:
                if (state | 1 << v, v) not in memo:
                    q.append((v, steps + 1, state | 1 << v))
                    memo.add((state | 1 << v, v))