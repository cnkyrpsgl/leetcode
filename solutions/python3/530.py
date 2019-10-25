# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.res = sys.maxsize
        def dfs(node):
            if not node: return sys.maxsize, -sys.maxsize
            lMn, lMx = dfs(node.left)
            rMn, rMx = dfs(node.right)
            self.res = min(self.res, node.val - lMx, rMn - node.val)
            return min(node.val, lMn), max(node.val, rMx)
        dfs(root)
        return self.res