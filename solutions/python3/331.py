class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for c in preorder.split(','):
            stack.append(c)
            while stack[-2:] == ['#', '#']:
                stack.pop()
                stack.pop()
                if not stack: return False
                stack.pop()
                stack.append('#')
        return stack == ['#']