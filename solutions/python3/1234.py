class Solution:
    def balancedString(self, s: str) -> int:
        cnt, i, res = {c: max(s.count(c) - len(s) // 4, 0) for c in 'QWER'}, 0, len(s)
        for j, c in enumerate(s):
            cnt[c] -= 1
            while i < len(s) and cnt[s[i]] < 0:
                cnt[s[i]] += 1
                i += 1
            if not any(cnt[c] > 0 for c in 'QWER'):
                res = min(res, j - i + 1)
        return res