class Solution:
    def calcEquation(self, equations, values, queries):
        def explore(x, y, r, q):
            results[(x, y)] = r
            for z in edges[y]:
                if z not in q:
                    results[(x, z)], results[(z, x)] = r * vals[(y, z)], 1 / (r * vals[(y, z)])
                    explore(x, z, r * vals[(y, z)], q | {z})
        edges, vals, visited, results, res = collections.defaultdict(set), {}, set(), {}, []
        for i, eq in enumerate(equations):
            edges[eq[0]].add(eq[1])
            edges[eq[1]].add(eq[0])
            vals[(eq[0], eq[1])], vals[(eq[1], eq[0])] = values[i], 1 / values[i]
        for i, eq in enumerate(equations):
            for p in eq:
                if p not in visited:
                    visited.add(p)
                    explore(p, p, 1.0, {p})
        for q in queries:
            if (q[0], q[1]) in results: res += results[(q[0], q[1])],
            else: res += -1.0,
        return res