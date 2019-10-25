# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def traverse(node):
            if not node: return
            left, right = traverse(node.left), traverse(node.right)
            if node.left: left.right, node.right, node.left = node.right, node.left, None
            return right if right else left if left else node
        traverse(root)