class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        q, depth = [root], 1
        while depth != d: parent, q, depth = q, [kid for node in q for kid in (node.left, node.right) if kid], depth+1
        if d != 1:
            for node in parent: node.left, node.right, node.left.left, node.right.right = TreeNode(v), TreeNode(v), node.left, node.right
            return root
        else: 
            first, first.left = TreeNode(v), root
            return first