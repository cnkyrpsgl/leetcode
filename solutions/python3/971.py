# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root, voyage):
        res = []
        self.i = 0
        def dfs(node):
            if not node: return True
            if node.val != voyage[self.i]:
                return False
            self.i += 1
            if node.left and node.left.val != voyage[self.i]:
                node.left, node.right = node.right, node.left
                res.append(node.val)
            return dfs(node.left) and dfs(node.right)
        return res if dfs(root) else [-1]