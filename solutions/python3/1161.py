# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        levels, l, q = [], 1, [root]
        while q:
            levels.append([sum(node.val for node in q), l])
            l += 1
            q = [child for node in q for child in (node.left, node.right) if child]
        return sorted(levels, key = lambda x: (x[0], -x[1]))[-1][1]