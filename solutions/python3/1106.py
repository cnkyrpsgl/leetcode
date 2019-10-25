class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for c in expression:
            if c == ')':
                cache = []
                while stack[-1] != '(':
                    cache.append(stack.pop())
                stack.pop()
                cur = stack.pop()
                stack.append(all(cache) if cur == '&' else any(cache) if cur == '|' else not cache.pop())
            elif c != ',':
                stack.append(True if c == 't' else False if c == 'f' else c)
        return stack.pop()        