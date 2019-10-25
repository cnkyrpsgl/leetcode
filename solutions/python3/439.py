class Solution:
    def parseTernary(self, expression, stack = []):
        for c in expression[::-1]:
            if stack and stack[-1] == "?":
                _, first, q, second = stack.pop(), stack.pop(), stack.pop(), stack.pop()
                stack.append(c == "T" and first or second)
            else:
                stack.append(c)
        return stack.pop()