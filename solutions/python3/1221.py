class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = cnt = 0         
        for c in s:
            cnt += c == 'L'
            cnt -= c == 'R'
            res += cnt == 0
        return res  