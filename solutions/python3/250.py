# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        res = [0]
        def dfs(node, value):
            if not node:
                return True, value
            left, lVal = dfs(node.left, node.val)
            right, rVal = dfs(node.right, node.val)
            cnt = left and right and lVal == rVal == node.val
            if cnt:
                res[0] += 1
            return cnt, node.val
        dfs(root, None)
        return res[0]