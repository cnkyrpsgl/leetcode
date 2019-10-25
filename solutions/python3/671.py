# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.sec = float('inf')
        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            if root.val < node.val < self.sec:
                self.sec = node.val
        dfs(root)
        return self.sec if self.sec < float('inf') else -1