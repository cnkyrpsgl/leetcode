class Solution:
    res = 0
    def minCameraCover(self, root):
        def dfs(root):
            if not root: return 2
            if not root.left and not root.right: return 0
            l, r = dfs(root.left), dfs(root.right)
            if l == 0 or r == 0:
                self.res += 1
                return 1
            if l == 1 or r == 1:
                return 2
            return 0
        return (dfs(root) == 0) + self.res