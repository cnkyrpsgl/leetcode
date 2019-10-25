class Solution:
    def smallestEquivalentString(self, A: str, B: str, S: str) -> str:
        def root(c):
            return c if parent[c] == c else root(parent[c])
        parent = {s: s for s in string.ascii_lowercase}
        for a, b in zip(A, B):
            p1, p2 = root(a), root(b)
            if p1 <= p2:
                parent[p2] = p1
            else:
                parent[p1] = p2
        return ''.join(root(s) for s in S)