# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        q, l = root and [(root, 1)] or [], 0
        while q:
            node, path = q.pop()
            l = max(l, path)
            q += [(child, child.val == node.val + 1 and path + 1 or 1) for child in (node.left, node.right) if child]
        return l