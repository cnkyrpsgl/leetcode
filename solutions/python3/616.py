class Solution:
    def addBoldTag(self, S, words):
        trie, n, mask, res = {}, len(S), set(), ""
        for w in words:
            cur = trie
            for c in w:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["#"] = cur.get("#", set()) | {w}
        for i in range(n):
            cur, j = trie, i
            while j < n and S[j] in cur:
                cur = cur[S[j]]
                if "#" in cur:
                    mask |= {ind for ind in range(i, j + 1)}
                j += 1
        for i in range(n):
            if i in mask and (not i or i - 1 not in mask):
                res += "<b>"
            res += S[i]
            if i in mask and (i == n - 1 or i + 1 not in mask):
                res += "</b>"
        return res