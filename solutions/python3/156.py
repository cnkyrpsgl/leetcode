# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root):
        if root:
            left = self.upsideDownBinaryTree(root.left)
            self.upsideDownBinaryTree(root.right)
            if root.left:
                root.left.right, root.left.left = root, root.right
                root.right = root.left = None
            return left or root