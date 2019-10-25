class Solution:
    def splitBST(self, root, V):
        if not root:
            return [None, None]
        if root.val == V:
            a = root.right
            root.right = None
            return [root, a]
        elif root.val < V:
            small, large = self.splitBST(root.right, V)
            root.right = small
            return [root, large]
        else:
            small, large = self.splitBST(root.left, V)
            root.left = large
            return [small, root]