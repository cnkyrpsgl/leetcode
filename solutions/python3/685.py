class Solution:
    def findRedundantDirectedConnection(self, edges):
        def root(i):
            return parent[i] == i and i or root(parent[i])
        
        parent, a, b, c = [0] * (len(edges) + 1), None, None, None
        for i, edge in enumerate(edges):
            if parent[edge[1]]:
                a, b, c, edges[i][0]= parent[edge[1]], edge[0], edge[1], 0
            else:
                parent[edge[1]] = edge[0]
        
        parent = [i for i in range(len(edges) + 1)]
        for u, v in edges:
            if u:
                if root(u) == v: 
                    return a and [a, c] or [u, v]
                parent[v] = u   
        return [b, c]