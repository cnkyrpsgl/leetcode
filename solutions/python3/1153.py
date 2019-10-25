class Solution:
    def canConvert(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        dp = {}
        for i, j in zip(s1, s2):
            if dp.setdefault(i, j) != j:
                return False
        return len(set(s2)) < 26