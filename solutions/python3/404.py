# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def left(node, sm):
            if not node: return
            left(node.left,sm)
            if node.left:
                if not node.left.left and not node.left.right: sm.append(node.left.val)
            left(node.right,sm)
        otp=list()
        left(root,otp)
        return sum(otp)