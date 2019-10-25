class Solution:
    def isBipartite(self, graph):
        side = [0] * len(graph)
        def dfs(node):
            for v in graph[node]:
                if side[v] == 0: 
                    side[v] = -side[node]
                    if not dfs(v): return False
                elif side[v] == side[node]: return False
            return True
        for i in range(len(graph)):
            if side[i] == 0: 
                side[i] = 1
            if not dfs(i): return False
        return True