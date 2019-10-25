class Solution:
    def reachableNodes(self, edges, M, N):
        adj, seen = collections.defaultdict(dict), set()
        for a, b, l in edges:
            adj[a][b] = [l, 0]
            adj[b][a] = [l, 0]
        q = [(0, M, None)]
        while q:
            new = []
            for i, moves, pre in q:
                seen.add(i)
                for j in adj[i]:
                    if moves > adj[i][j][1]:
                        adj[i][j][1] = moves
                        if moves > adj[i][j][0] and j != pre:
                            new.append((j, moves - adj[i][j][0] - 1, i))
            q = new 
        return sum(min(adj[i][j][1] + adj[j][i][1], l) for i, j, l in edges) + len(seen)