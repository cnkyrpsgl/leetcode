class Solution:
    def minRemoveToMakeValid(
        self, s: str, res: str = "", l: str = "(", r: str = ")", b: int = 0
    ) -> str:
        for _ in range(2):
            for c in s:
                if c == r and b <= 0:
                    continue
                b += c == l
                b -= c == r
                res += c
            res, s, l, r, b = "", res[::-1], r, l, 0
        return s
