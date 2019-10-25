class Solution:
    def minMalwareSpread(self, graph, initial):
        def dfs(i):
            seen.add(i)
            return not any(graph[i][j] and j not in seen and (j in initials or not dfs(j)) for j in range(len(graph[i])))
        res, mx, initials = min(initial), 1, set(initial)
        for node in sorted(initial):
            impact = set()
            for j in range(len(graph[node])):
                seen = {node}
                if graph[node][j] and j not in initials and dfs(j): impact |= seen
            if len(impact) > mx: res, mx = node, len(impact)
        return res