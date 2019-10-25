# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = [root]
        q = [root]
        while any(q):
            tmp = []
            for node in q:
                if node.right:
                    res.insert(res.index(node) + 1, node.right)
                    tmp.append(node.right)
                if node.left:
                    res.insert(res.index(node) + 1, node.left)
                    tmp.insert(-1, node.left)
            q = tmp
        return [j.val for j in res if j]