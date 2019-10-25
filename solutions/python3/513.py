# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        bfs = [root]
        while bfs:
            left = bfs[0].val
            bfs = [child for node in bfs for child in (node.left, node.right) if child]
        return left