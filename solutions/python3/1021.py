class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        l = r = 0
        res = cur = ''
        for s in S:
            cur += s
            l += s == '('
            r += s == ')'
            if l == r:
                res += cur[1:-1]
                cur = ''
        return res 