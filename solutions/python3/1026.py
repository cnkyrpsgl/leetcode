# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            mx = mn = node.val
            if node.left:
                lMn, lMx = dfs(node.left)
                mx = max(mx, lMx)
                mn = min(mn, lMn)
                self.res = max(self.res, abs(lMn - node.val), abs(lMx - node.val))
            if node.right:
                rMn, rMx = dfs(node.right)
                mx = max(mx, rMx)
                mn = min(mn, rMn)
                self.res = max(self.res, abs(rMn - node.val), abs(rMx - node.val))
            return mn, mx
        dfs(root)
        return self.res