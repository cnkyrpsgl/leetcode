class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i, c in enumerate(s):
            if not stack or stack[-1][0] != c:
                stack.append([c, 1])
            else:
                stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        return ''.join(k * v for k, v in stack) 
                