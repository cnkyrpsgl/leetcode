class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        c1 = collections.Counter(A.split())
        c2 = collections.Counter(B.split())
        return list(c for c in c1 if c1[c] == 1 and c not in c2) + list(c for c in c2 if c2[c] == 1 and c not in c1)