# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.compute(root)     
    def compute(self, node):
        if not node: return 0
        left_d=self.compute(node.left)
        right_d=self.compute(node.right)
        if node.left and node.right: return min(left_d,right_d)+1
        else: return max(left_d,right_d)+1