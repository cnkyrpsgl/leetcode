# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q, i, res = [root], 0, []
        while any(q):
            add, q, i = q if i % 2 == 0 else q[::-1], [kid for node in q for kid in (node.left, node.right) if kid], i+1
            res.append([item.val for item in add])
        return res