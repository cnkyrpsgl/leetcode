class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score += h > 8
            score -= h < 9
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res