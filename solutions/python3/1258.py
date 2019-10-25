class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        def root(s):
            return s if parent[s] == s else root(parent[s])

        parent = {s: s for s in [c for sy in synonyms for c in sy] + text.split()}
        for a, b in synonyms:
            parent[root(a)] = root(b)
        bfs = [""]
        for t in text.split():
            r = root(t)
            bfs = [s + " " + w for s in bfs for w in parent if root(w) == r]
        return sorted(s[1:] for s in bfs)
