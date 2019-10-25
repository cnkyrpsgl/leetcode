class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for w in queries:
            j = 0
            for c in w:
                if j < len(pattern) and c == pattern[j]:
                    j += 1
                elif c.isupper():
                    j = len(pattern) + 1
            res.append(j == len(pattern))
        return res