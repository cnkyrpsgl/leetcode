class Solution:
    def accountsMerge(self, accounts):
        def explore(mail, q):
            q += mail,
            visited.add(mail)
            for v in edges[mail]:
                if v not in visited: explore(v, q)
            return q
        edges, owner, visited, res = collections.defaultdict(list), {}, set(), []
        for acc in accounts:
            owner[acc[1]] = acc[0]
            for i in range(1, len(acc) - 1): 
                if acc[i] != acc[i + 1]:
                    edges[acc[i]] += acc[i + 1],
                    edges[acc[i + 1]] += acc[i],
        for acc in accounts:
            if acc[1] not in visited: res += [acc[0]] + sorted(explore(acc[1], [])),
        return res