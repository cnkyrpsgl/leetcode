class Solution:
    def eventualSafeNodes(self, graph):
        def explore(i):
            visited[i] = 0
            for v in graph[i]:
                if visited[v] == 0 or (visited[v] == -1 and explore(v)): return True
            visited[i] = 1
            res.append(i)
            return False
        visited, res = [-1] * len(graph), []
        for i in range(len(graph)):
            if visited[i] == -1: explore(i)
        return sorted(res)