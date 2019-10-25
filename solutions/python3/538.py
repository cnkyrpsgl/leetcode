# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def traverse(node):
            if not node: return
            traverse(node.right)
            node.val = residue[0] = node.val + residue[0]
            traverse(node.left)
            return node
        residue = [0]
        return traverse(root)