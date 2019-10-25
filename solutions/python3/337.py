class Solution:
    def rob(self, root):
        def dfs(node):
            if not node: return 0, 0
            l, r = dfs(node.left), dfs(node.right)
            return max(l) + max(r), node.val + l[0] + r[0]
        return max(dfs(root))