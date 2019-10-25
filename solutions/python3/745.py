class WordFilter:
    def __init__(self, words):
        self.p, self.s, self.ind = collections.defaultdict(set), collections.defaultdict(set), {}
        for i, w in enumerate(words): 
            self.ind[w] = i
            self.p[""].add(w)
            self.s[""].add(w)
            for i in range(1, len(w) + 1): 
                self.p[w[:i]].add(w)
                self.s[w[-i:]].add(w)
    def f(self, prefix, suffix): return max((self.ind[c] for c in self.p[prefix] & self.s[suffix]), default = -1)