# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node, q):
            if not node: return
            traverse(node.left, q + [str(node.val)])
            traverse(node.right, q + [str(node.val)]) 
            if not node.left and not node.right: res[0] += int("".join(q + [str(node.val)]))
        res = [0]
        traverse(root, [])
        return res[0]