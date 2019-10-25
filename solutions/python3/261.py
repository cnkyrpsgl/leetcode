class Solution:
    def validTree(self, n, edges):
        visited, adj = [0] * n, collections.defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        def dfs(i, pre):
            visited[i] = 1
            for v in adj[i]:
                if v != pre and (visited[v] or not dfs(v, i)):
                    return False
            return True
        return dfs(0, -1) and sum(visited) == n