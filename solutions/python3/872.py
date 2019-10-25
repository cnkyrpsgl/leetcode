class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node, arr):
            if node:
                if not node.left and not node.right: arr += [node.val]
                dfs(node.left, arr)
                dfs(node.right, arr)
                return arr
        return dfs(root1, []) == dfs(root2, [])