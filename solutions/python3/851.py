class Solution:
    def loudAndRich(self, richer, quiet):
        edges, memo, res = collections.defaultdict(list), {}, [i for i in range(len(quiet))]
        for r, p in richer: edges[p].append(r)
        def explore(i):
            if i in memo: return memo[i]
            cur_min = i
            for v in edges[i]:
                cur = explore(v)
                if quiet[cur] < quiet[cur_min]: cur_min = cur
            res[i] = memo[i] = cur_min
            return cur_min
        for i in range(len(quiet)): explore(i)
        return res