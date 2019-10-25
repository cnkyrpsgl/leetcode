# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def str2tree(self, s):
        stack, cur = [], ""
        for i, c in enumerate(s):
            if c.isnumeric() or c == "-":
                cur += c
            elif not cur:
                if c == ")":
                    stack.pop()
            else:
                node = TreeNode(int(cur))
                if stack:
                    if not stack[-1].left:
                        stack[-1].left = node
                    else:
                        stack[-1].right = node
                cur = ""
                if c == "(":
                    stack.append(node)
        return stack and stack[0] or (cur and TreeNode(int(cur))) or []