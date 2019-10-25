# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        
        def dfs(node, parent):
            if not node: return True
            dfs(node.left, node)
            dfs(node.right, node)
            if node.val in blacklist:
                if parent and parent.left == node:
                    parent.left = None
                elif parent:
                    parent.right = None
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
        res = []
        blacklist = set(to_delete)
        dfs(root, None)
        return res + [root] if root.val not in blacklist else res