# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root):
        res = []
        def dfs(node):
            if not node: return -1
            i = max(dfs(node.left), dfs(node.right)) + 1
            try: res[i].append(node.val)
            except: res.append([node.val])
            return i
        dfs(root)
        return res