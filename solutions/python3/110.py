# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.computeHeight(root)!=-1
    def computeHeight(self, node):
        if not node: return 0
        left_h=self.computeHeight(node.left)
        right_h=self.computeHeight(node.right)
        if left_h==-1 or right_h==-1 or abs(left_h-right_h)>1: return -1    
        return max(left_h,right_h)+1