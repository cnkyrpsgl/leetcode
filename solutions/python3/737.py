class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        def dfs(node, Id):
            cc[node] = Id
            for v in adj[node]:
                if v not in cc:
                    dfs(v, Id)
        l1, l2, adj, cc = len(words1), len(words2), collections.defaultdict(set), {}
        if l1 != l2:
            return False
        for a, b in pairs:
            adj[a].add(b)
            adj[b].add(a)
        for Id, k in enumerate(adj):
            if k not in cc:
                dfs(k, Id)
        for w1, w2 in zip(words1, words2):
            if w1 not in cc or w2 not in cc:
                if w1 != w2:
                    return False
            elif cc[w1] != cc[w2]:
                return False
        return True