class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for i in S:
            if i == 'c':
                if stack[-2:] != ['a', 'b']:
                    return False
                stack.pop()
                stack.pop()
            else:
                stack.append(i)
        return not stack