class Solution:
    def countComponents(self, n, edges):
        visited, res, adj = set(), 0, collections.defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        def dfs(i):
            visited.add(i)
            for v in adj[i]:
                if v not in visited:
                    dfs(v)
        for i in range(n):
            if i not in visited:
                res += 1
                dfs(i)
        return res