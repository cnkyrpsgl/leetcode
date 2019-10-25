# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validate(node, mn, mx):
            if not node: return True
            if node.val<mn or node.val>mx: return False
            return validate(node.left,mn,node.val-1) and validate(node.right,node.val+1,mx)
        return validate(root, -float("inf"),float("inf"))