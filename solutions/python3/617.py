class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            root, root.left, root.right = TreeNode(t1.val + t2.val), self.mergeTrees(t1.left, t2.left), self.mergeTrees(t1.right, t2.right)
            return root
        else: return t1 or t2