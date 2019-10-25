# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q, res = [root], []
        while any(q):
            res.append([i.val for i in q])
            q = [kid for node in q for kid in (node.left, node.right) if kid]
        return res