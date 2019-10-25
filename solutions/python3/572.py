class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def traverse(node):
            if not node: return "^"
            return "$"+str(node.val)+"?"+traverse(node.left)+"@"+traverse(node.right)
        return traverse(t) in traverse(s)