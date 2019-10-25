# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def traverse(node, q, residue, res = []):
            if node:
                if not node.left and not node.right and residue + node.val == sum: res.append(q + [node.val])
                traverse(node.left, q + [node.val], residue + node.val)
                traverse(node.right, q + [node.val], residue + node.val)
            return res
        return traverse(root, [], 0)