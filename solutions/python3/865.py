# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.l = 0
        self.nodes = set()
        self.res = 0
        def dfs(node, l):
            if node:
                if l > self.l:
                    self.nodes = {node.val}
                    self.l = l
                elif l == self.l:
                    self.nodes.add(node.val)
                dfs(node.left, l + 1)
                dfs(node.right, l + 1)
        def dfs2(node):
            if not node: return set()
            l = dfs2(node.left)
            r = dfs2(node.right)
            total = l | r | {node.val}
            if total & self.nodes == self.nodes:
                self.res = node
                return set()
            return total
        dfs(root, 0)
        dfs2(root)
        return self.res