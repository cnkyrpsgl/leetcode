class Solution:
    def smallestFromLeaf(self, root: TreeNode, s = '') -> str:
        if not root.right and not root.left:
            return chr(97 + root.val) + s
        if not root.right:
            return self.smallestFromLeaf(root.left, chr(97 + root.val) + s)
        if not root.left:
            return self.smallestFromLeaf(root.right, chr(97 + root.val) + s)
        return min(self.smallestFromLeaf(root.left, chr(97 + root.val) + s), self.smallestFromLeaf(root.right, chr(97 + root.val) + s))