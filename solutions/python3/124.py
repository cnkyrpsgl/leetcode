class Solution:
    def maxPathSum(self, root):
        res = [-float("inf")]
        def dfs(node):
            if not node: return -float("inf")
            l, r = dfs(node.left), dfs(node.right)
            mx = max(node.val, l + node.val, r + node.val)
            res[0] = max(res[0], mx, node.val + l + r)
            return mx
        dfs(root)
        return res[0]