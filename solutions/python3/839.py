class Solution:
    def numSimilarGroups(self, A):
        def explore(s):
            visited.add(s)
            for v in edges[s]:
                if v not in visited: explore(v)
        res, edges, visited = 0, {}, set()
        if len(A) >= 2 * len(A[0]):
            strs = set(A)
            for s in A:
                if s not in edges: edges[s] = set()
                for i in range(len(s) - 1):
                    for j in range(i + 1, len(s)):
                        new = s[:i] + s[j] + s[i + 1:j] + s[i] + s[j + 1:]
                        if new in strs:
                            edges[s].add(new)
                            if new in edges: edges[new].add(s)
                            else: edges[new] = {s}
        else:
            for s in A:
                if s not in edges: edges[s] = set()
                for t in A:
                    if s != t:
                        same = 0
                        for i, c in enumerate(t):
                            if c == s[i]: same += 1
                        if same == len(s) - 2: 
                            edges[s].add(t)
                            if t in edges: edges[t].add(s)
                            else: edges[t] = {s}
        for s in A:
            if s not in visited:
                res += 1
                explore(s)
        return res              