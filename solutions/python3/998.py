class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int, parent = None) -> TreeNode:
        if not root or val > root.val:
            new = TreeNode(val)
            new.left = root
            if parent:
                if parent.right == root:
                    parent.right = new
                else:
                    parent.left = new
            root = new
        else:
            root.right = self.insertIntoMaxTree(root.right, val, root)
        return root