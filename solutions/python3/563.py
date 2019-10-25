# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node):
            if not node: return 0
            left = traverse(node.left)
            right = traverse(node.right)
            res.append(abs(right -left))
            return node.val + left + right
        res = []
        traverse(root)
        return sum(res)