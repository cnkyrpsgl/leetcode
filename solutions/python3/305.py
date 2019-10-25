class Solution:
    def numIslands2(self, m, n, positions):
        def getParent(i):
            if i != parent[i]:
                parent[i] = getParent(parent[i])
            return parent[i]
        islands, res, parent, Id = set(), [], {}, 1
        for i, j in positions:
            parent[(i, j)] = parent[Id] = Id
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if (x, y) in parent:
                    p = getParent(parent[(x, y)])
                    islands.discard(p)
                    parent[p] = Id
            islands.add(Id)
            Id += 1
            res.append(len(islands))
        return res