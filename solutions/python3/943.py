class Solution:
    def shortestSuperstring(self, A):
        def merge(a, b):
            for i in range(len(b), 0, -1):
                if a.endswith(b[:i]):
                    return i
            return 0
        def dfs(sup, s, st):
            if len(sup + "".join(st)) < len(res[0]):
                res[0] = sup + "".join(st)
            if st and any(new in st for new in merged[s][1:]):
                for new in merged[s][1:]:
                    if new in st:
                        dfs(sup + new[merged[s][0]:], new, st - {new})
            else:
                for nex in st:
                    for new in merged[nex][1:]:
                        if new in st:
                            dfs(sup + nex + new[merged[nex][0]:], new, st - {nex, new})
        merged = {}
        for a, b in itertools.combinations(A, 2):
            for a, b in ((a, b), (b, a)):
                s = merge(a, b)
                if a not in merged or s > merged[a][0]:
                    merged[a] = [s, b]
                elif s == merged[a][0]:
                    merged[a].append(b)
        res, st = ["".join(A)], set(A)
        for a in A:
            dfs(a, a, st - {a})
        return res[0]