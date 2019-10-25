class Solution:
    def generatePalindromes(self, s):
        cnt, n = collections.Counter(s), len(s) // 2
        odd, s, q = [c for c in cnt if cnt[c] % 2], "".join(k * (cnt[k] // 2) for k in cnt), {"#" * n}
        if len(odd) > 1: return []
        for c in s:
            new = set()
            for w in q:
                for i in range(n):
                    if w[i] == "#":
                        new.add(w[:i] + c + w[i + 1:])
            q = new
        return [w + odd[0] + w[::-1] for w in q] if odd else [w + w[::-1] for w in q]