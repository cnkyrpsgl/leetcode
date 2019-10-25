class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1: return [0]
        adj = [set() for i in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)
            newleaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1: 
                    newleaves.append(j)
            leaves = newleaves
        return leaves 