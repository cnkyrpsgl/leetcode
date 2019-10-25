class Solution:
    def longestValidParentheses(self, s):
        stack, mx = [], 0
        for i, c in enumerate(s):
            if c == ")" and stack and s[stack[-1]] == "(": stack.pop()
            else: stack.append(i)
        stack = [-1] + stack + [len(s)]
        for i1, i2 in zip(stack, stack[1:]): mx = max(mx, i2 - i1 - 1)
        return mx if len(stack) > 2 else len(s)