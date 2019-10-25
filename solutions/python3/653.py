class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def traverse(node):
            if not node: return False
            if not node.val in dic: dic[k-node.val]=1
            else: return True
            return traverse(node.left) or traverse(node.right)
        dic={}
        return traverse(root)