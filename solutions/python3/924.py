class Solution:
    def minMalwareSpread(self, graph, initial):
        def dfs(i):
            nodes.add(i)
            for j in range(len(graph[i])):
                if graph[i][j] and j not in nodes:
                    dfs(j)
        rank, initial = collections.defaultdict(list), set(initial)
        for node in sorted(initial):
            nodes = set()
            dfs(node)
            if nodes & initial == {node}:
                rank[len(nodes)].append(node)
        return rank[max(rank)][0] if rank else min(initial)