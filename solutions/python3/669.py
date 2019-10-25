# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root: return
        root.left=self.trimBST(root.left,L,R)
        root.right=self.trimBST(root.right,L,R)
        if root.val>R or root.val<L: return root.left if root.left else root.right
        return root