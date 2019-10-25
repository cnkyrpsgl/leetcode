# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root: return []
        used, res, r = {root}, [root.val], []
        def lb(node):
            if node not in used:
                used.add(node)
                res.append(node.val)
            if node.left:
                lb(node.left)
            elif node.right:
                lb(node.right)
        def rb(node):
            if node not in used:
                used.add(node)
                r.append(node.val)
            if node.right:
                rb(node.right)
            elif node.left:
                rb(node.left)
        def lv(node):
            if not node.left and not node.right and node not in used:
                used.add(node)
                res.append(node.val)
            if node.left:
                lv(node.left)
            if node.right:
                lv(node.right)
        if root.left:
            lb(root.left)
        lv(root)
        if root.right:
            rb(root.right)
        return res + r[::-1]