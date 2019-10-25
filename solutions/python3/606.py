class Solution:        
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ""
        parent="%s" %t.val
        left, right= "", ""
        if t.left or t.right: left= "(%s)" % self.tree2str(t.left)
        if t.right: right= "(%s)" % self.tree2str(t.right)
        return parent+left+right       