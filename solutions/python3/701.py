class Solution:
    def insertIntoBST(self, root, val):
        if root and root.val > val and not self.insertIntoBST(root.left, val): root.left = TreeNode(val)
        elif root and root.val < val and not self.insertIntoBST(root.right, val): root.right = TreeNode(val)
        return root