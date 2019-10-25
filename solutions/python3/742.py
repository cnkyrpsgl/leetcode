# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findClosestLeaf(self, root, k):
        adj, q, visited = collections.defaultdict(list), [], collections.defaultdict(int)
        def dfs(node):
            if node:
                if node.val == k:
                    q.append(node)
                    visited[node.val] = 1
                if node.left:
                    adj[node].append(node.left)
                    adj[node.left].append(node)
                    dfs(node.left)
                if node.right:
                    adj[node].append(node.right)
                    adj[node.right].append(node)
                    dfs(node.right)
        dfs(root)
        while q:
            new = []
            for node in q:
                if not node.left and not node.right:
                    return node.val
                for v in adj[node]:
                    if not visited[v.val]:
                        visited[v.val] = 1
                        new.append(v)
            q = new                