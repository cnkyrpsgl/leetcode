class Solution:
    val = 0
    def bstToGst(self, root):
        if root.right: self.bstToGst(root.right)
        root.val = self.val = self.val + root.val
        if root.left: self.bstToGst(root.left)
        return root