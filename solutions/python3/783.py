class Solution:
    def minDiffInBST(self, root):
        def dfs(node):
            if not node: return float("inf"), float("inf"), -float("inf")
            l, lMn, lMx = dfs(node.left)
            r, rMn, rMx = dfs(node.right)
            return min(l, node.val - lMx, r, rMn - node.val), min(lMn, node.val), max(rMx, node.val)
        return dfs(root)[0]