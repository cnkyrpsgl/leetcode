class Solution:
    def scoreOfParentheses(self, S):
        stack, res = [], 0
        for c in S:
            if c == "(":
                stack.append(0)
            else:
                add = 2 * stack.pop() or 1
                if stack:
                    stack[-1] += add
                else:
                    res += add
        return res