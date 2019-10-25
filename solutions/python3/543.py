# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def traverse(node):
            if not node: return 0
            left, right = traverse(node.left), traverse(node.right)
            res[0] = max(left+right, res[0])
            return 1+ max(left, right)
        traverse(root)
        return res[0]