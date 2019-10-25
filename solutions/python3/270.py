# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        res, d = [0], [float("inf")]
        def dfs(node):
            if node:
                new = node.val - target if node.val >= target else target - node.val
                if new < d[0]:
                    d[0] = new
                    res[0] = node.val
                if target < node.val:
                    dfs(node.left)
                else:
                    dfs(node.right)
        dfs(root)
        return res[0]