# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestKValues(self, root, target, k):
        d = []
        def dfs(node):
            if node:
                heapq.heappush(d, (abs(node.val - target), node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return [node for val, node in heapq.nsmallest(k, d)]